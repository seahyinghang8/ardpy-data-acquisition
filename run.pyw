import wx
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import serial.tools.list_ports as list_ports
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#import the GUI file 
import imre_gui as gui



class MainFrame(gui.FrameMain): 
    def __init__(self, parent): 
        gui.FrameMain.__init__(self,parent)

        # initializing variables
        self.start_time = 0.0       # start time for referencing
        self.filename = ""          # filename for file I/O
        self.init_line = ""         # the first line of file to be reused
        self.initial_counter = 0    # the number of characters to be removed from the start of file
        self.com = ""               # COM port of arduino for serial
        self.chart_num = 0          # number of charts that user want to display
        self.pause = True           # to decide whether acquisition stops


    def animateMain(self, i, line, xdata, ydata, ax, arduino, y_array):
        if self.pause:
            arduino.close()
            return

        arduino.write("1")

        time.sleep(0.48)

        # split data into arrays
        raw_data = arduino.readline().rstrip().split(",")
        processed_data = ""
        
        # record time
        recorded_time = round((time.clock() - self.start_time), 2)

        # process data
        index = 0
        for data in raw_data:
            if (index < self.chart_num):
                new_data = round((float(data) / 1023.0 * 5000.0), 2)
                processed_data += "\t%.2f" %(new_data)
                y_array[index].append(new_data)
            index += 1

        # confirmation in command line
        print round(recorded_time, 1), processed_data
        # update timer
        self.timerDisplay.SetValue("%d" %(round(recorded_time)))
        to_be_written = "\n%.2f%s" %(recorded_time, processed_data)

        # file I/O
        datafile = open(self.filename, "a")
        datafile.write(to_be_written)
        datafile.close()

        # append to arrays
        xdata.append(recorded_time)
        # update plot
        line.set_data([xdata, ydata])
        # rescale the plots
        ax.relim()
        ax.autoscale_view()

        return line,


    def animateSide(self, i, line, xdata, ydata, ax):
        if self.pause:
            return

        # update plot
        line.set_data([xdata, ydata])
        # rescale the plots
        ax.relim()
        ax.autoscale_view()

        return line,


    def start(self, event):
        # check if any plots are still opened
        if plt.get_fignums():
            self.showMessage("Close all previous plots before starting new record.")
            return

        # check if arduino port is available. if not, cancel.
        ports = list(list_ports.comports())
        port_exist = False

        for p in ports:
            if "Arduino" in p[1]:
                print "Arduino detected!"
                self.com = p[0]
                port_exist = True

        if port_exist:
            print "Save file to begin data acquisition..."

            # initialize and fire up the file dialog
            fd = wx.FileDialog(self,message="Save data as...",style=wx.FD_SAVE,
                                   wildcard="Dat file (*.dat)|*.dat")
            fd.ShowModal()

            # get filename if possible and proceed to save
            self.filename = fd.GetPath()

             # check if filename exists or user clicked cancel
            if self.filename:
                self.saveAndStart()
                return
        else:
            self.showMessage("Arduino is NOT detected. Connect Arduino to START.")
            return
       


    def end(self, event):
        # end all animation
        self.pause = True

        # get the values from the 3 lines
        line1 = self.input1.GetValue()
        line2 = self.input2.GetValue()
        line3 = self.input3.GetValue()

        # getting ready
        to_be_written = "%s\n%s\n%s\n%s\n" %(self.init_line, line1, line2, line3)

        # open up the file
        datafile = open(self.filename, "r+")
        # read and replace
        raw_data = datafile.read()
        datafile.close()
        # create new data
        new_data = to_be_written + raw_data[self.initial_counter:]
        # transferred new data
        newfile = open(self.filename, "w")
        newfile.write(new_data)
        newfile.close()

        # set the filePicker value to be the empty
        self.filePicker1.SetPath("")
        # enable start button
        self.button1.Enable()
        # enable chart picker
        self.choice1.Enable()
        # disable end button
        self.button2.Disable()

    def showMessage(self, message):
        wx.MessageBox(message, "Note", 
            wx.OK | wx.ICON_INFORMATION)

    def saveAndStart(self):
        # get the first line
        self.init_line = "#HD " + time.strftime("%Y %m %d %H %M")
        # get the values from the 3 lines
        line1 = self.input1.GetValue()
        line2 = self.input2.GetValue()
        line3 = self.input3.GetValue()
        # line to be written into the file
        to_be_written = "%s\n%s\n%s\n%s\n" %(self.init_line, line1, line2, line3)
        # update the counter
        self.initial_counter = len(to_be_written)

        # create the file
        datafile = open(self.filename, "w+")
        # write the first 3 lines
        datafile.write(to_be_written)
        # close the file to ensure values are saved
        datafile.close()

        # set the filePicker value to be the value of the file
        self.filePicker1.SetPath(self.filename)
        # disable start button
        self.button1.Disable()
        # disable chart picker
        self.choice1.Disable()
        # enable end button
        self.button2.Enable()
        # set timer to 0s
        self.timerDisplay.SetValue("0")


        # begin data acquisition
        # set variables
        self.chart_num = self.choice1.GetCurrentSelection() + 2
        time_interval = 500
        xdata = []
        y1data = []
        y2data = []
        y3data = []
        y4data = []
        y_array = [y1data, y2data, y3data, y4data]
        self.pause = False

        # setup serial b/w ard and python
        arduino = serial.Serial(self.com, 9600, timeout=1) 

        print "Waiting for serial communication to initialize..."
        time.sleep(1.5)

        # check number of charts to decide subplot orientation
        sp1 = 0
        sp2 = 0

        if (self.chart_num == 1):
            sp1 = 111
        elif (self.chart_num == 2):
            sp1 = 212
            sp2 = 211
        elif (self.chart_num == 3):
            sp1 = 313
            sp2 = 312
            sp3 = 311
        else:
            sp1 = 414
            sp2 = 413
            sp3 = 412
            sp4 = 411


        fig = plt.figure(figsize=(12,7))
        # initialize subplot1
        ax1 = fig.add_subplot(sp1)
        plt.title("Reading 1")
        plt.xlabel("Time (s)")
        plt.ylabel("X (mV)")

        ax1.relim()
        ax1.autoscale_view()

        y1line, = plt.plot([], [], "r-")
        ani1 = animation.FuncAnimation(fig, self.animateMain, fargs=(y1line, xdata, y1data, ax1, arduino, y_array), interval=time_interval)

        if (self.chart_num > 1):
            # initialize subplot 2
            ax2 = fig.add_subplot(sp2)
            plt.title("Reading 2")
            plt.xlabel("Time (s)")
            plt.ylabel("Y (mV)")

            ax2.relim()
            ax2.autoscale_view()

            y2line, = plt.plot([], [], "b-")
            ani2 = animation.FuncAnimation(fig, self.animateSide, fargs=(y2line, xdata, y2data, ax2), interval=time_interval)

        if (self.chart_num > 2):
            # initialize subplot 3
            ax3 = fig.add_subplot(sp3)
            plt.title("Reading 3")
            plt.xlabel("Time (s)")
            plt.ylabel("Y (mV)")

            ax3.relim()
            ax3.autoscale_view()

            y3line, = plt.plot([], [], "k-")
            ani3 = animation.FuncAnimation(fig, self.animateSide, fargs=(y3line, xdata, y3data, ax3), interval=time_interval)
        
        if (self.chart_num > 3):
            # initialize subplot 4
            ax4 = fig.add_subplot(sp4)
            plt.title("Reading 4")
            plt.xlabel("Time (s)")
            plt.ylabel("Y (mV)")

            ax4.relim()
            ax4.autoscale_view()

            y4line, = plt.plot([], [], "m-")
            ani4 = animation.FuncAnimation(fig, self.animateSide, fargs=(y4line, xdata, y4data, ax4), interval=time_interval)

        print "Commence data acquisition."
        self.start_time = time.clock() + 0.49
        plt.tight_layout()
        plt.show()






# initialize filename
app = wx.App(False) 
frame = MainFrame(None) 
frame.Show(True) 
#start the applications
print "Application running... Do NOT close this window."
app.MainLoop() 