import wx
from wx.lib.pubsub import pub
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import serial.tools.list_ports as list_ports

import threading

from multiprocessing import Process, Pipe
import time

#import the GUI file 
import imre_gui as gui

port_configured = False


class VoltageThread(threading.Thread):
    def __init__(self, parent, arduino):
        threading.Thread.__init__(self)
        """
        @param parent: the gui object that receives the value
        @param arduino: the serial object
        """
        self._parent = parent
        self._arduino = arduino
        self._continue = 1
        self.setDaemon(1)

    def run(self):
        global port_configured

        wx.CallAfter(pub.sendMessage, "set_status", status="Intializing serial communication...")

        # sleep time has to be longer than the usual readout to ensure previous thread is killed
        print "Serial communication initializing... Please wait a moment."

        time.sleep(2)

        self._arduino.write("1")

        time.sleep(0.5)

        # check whether there is any response
        if self._arduino.readline():
            port_configured = True
            wx.CallAfter(pub.sendMessage, "set_status", status="Port is functioning. Ready to start.")
        else:
            port_configured = False
            wx.CallAfter(pub.sendMessage, "set_status", status="Port Error. Try again or restart the program.")
            wx.CallAfter(pub.sendMessage, "show_message", message="Port is not functioning. Check if arduino is properly configured or restart the program.")
            return
            
        while self._continue and self._arduino.isOpen():
            self._arduino.write("1")

            time.sleep(0.48)

            # double check if port is still open
            if self._arduino.isOpen():
                # split data into arrays
                raw_data = self._arduino.readline().rstrip().split(",")
                values = []
                
                # process data
                for data in raw_data:
                    new_data = round((float(data) / 1023.0 * 5000.0), 2)
                    values.append(new_data)

                # publisher to send to update the voltage
                wx.CallAfter(pub.sendMessage, "update_voltage", values=values)
            else:
                # clear the current field
                wx.CallAfter(pub.sendMessage, "update_voltage", values=[])

    def abort(self):
        # kill worker thread
        self._continue = 0
        self._arduino.close()

class TimerThread(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)

        self._conn = conn
        self._continue = 1

    def run(self):
        while self._continue:
            time = self._conn.recv()
            wx.CallAfter(pub.sendMessage, "update_timer", time=time)


    def abort(self):
        self._continue = 0


class AnimationWorker(Process):
    def __init__(self, conn, port, chart_num, filename):
        Process.__init__(self)

        self._continue = 1
        self._pause = False
        self._conn = conn
        self._port = port
        self._chart = chart_num
        self._filename = filename

    def run(self):
        arduino = serial.Serial(self._port, 9600, timeout=1)

        time.sleep(2)

        time_interval = 500
        xdata = []
        y1data = []
        y2data = []
        y3data = []
        y4data = []
        y_array = [y1data, y2data, y3data, y4data]
        
        # check number of charts to decide subplot orientation
        if (self._chart == 0 or self._chart == 1):
            sp1 = 212
            sp2 = 211
        elif (self._chart == 2):
            sp1 = 313
            sp2 = 312
            sp3 = 311
        elif (self._chart == 3):
            sp1 = 221
            sp2 = 222
            sp3 = 223
            sp4 = 224


        fig = plt.figure(figsize=(12,7))
        # initialize subplot1
        ax1 = fig.add_subplot(sp1)
        plt.ylabel("X (mV)")

        ax1.relim()
        ax1.autoscale_view()

        y1line, = plt.plot([], [], "r-")
        ani1 = animation.FuncAnimation(fig, self.animateMain, fargs=(y1line, xdata, y1data, ax1, arduino, y_array), interval=time_interval)

        # initialize subplot 2
        ax2 = fig.add_subplot(sp2)
        plt.ylabel("Y (mV)")

        ax2.relim()
        ax2.autoscale_view()

        y2line, = plt.plot([], [], "b-")
        ani2 = animation.FuncAnimation(fig, self.animateSide, fargs=(y2line, xdata, y2data, ax2), interval=time_interval)

        if (self._chart > 1):
            # initialize subplot 3
            ax3 = fig.add_subplot(sp3)
            plt.ylabel("Z (mV)")

            ax3.relim()
            ax3.autoscale_view()

            y3line, = plt.plot([], [], "k-")
            ani3 = animation.FuncAnimation(fig, self.animateSide, fargs=(y3line, xdata, y3data, ax3), interval=time_interval)


        if (self._chart > 2):
            # initialize subplot 4
            ax4 = fig.add_subplot(sp4)
            plt.ylabel("A (mV)")

            ax4.relim()
            ax4.autoscale_view()

            y4line, = plt.plot([], [], "k-")
            ani4 = animation.FuncAnimation(fig, self.animateSide, fargs=(y4line, xdata, y4data, ax4), interval=time_interval)

        print "Commence data acquisition."

        self.start_time = time.time() + 0.49

        plt.tight_layout()
        plt.show()

    # animation to update graph for each data point collected
    def animateMain(self, i, line, xdata, ydata, ax, arduino, y_array):
        if not self._continue:
        	return

        if self._conn.poll():
            message = self._conn.recv()
            print message

            if message == 1:
            	self._conn.send(1)
                self._conn.close()
                self._continue = 0
                arduino.close()
                return

        arduino.write("1")

        time.sleep(0.48)

        if arduino.isOpen():
            # split data into arrays
            raw_data = arduino.readline().rstrip().split(",")
            processed_data = ""
            
            # record time
            recorded_time = round((time.time() - self.start_time), 2)

            # process data
            val1 = round((float(raw_data[0]) / 1023.0 * 5000.0), 2)
            val2 = round((float(raw_data[1]) / 1023.0 * 5000.0), 2)
            val3 = round((float(raw_data[2]) / 1023.0 * 5000.0), 2)
            val4 = round((float(raw_data[3]) / 1023.0 * 5000.0), 2)

            # appending values to y_array
            y_array[0].append(val1)

            if self._chart == 0:
                # chart processing for (2 - 3)
                diff = val2 - val3
                processed_data = "\t%.2f\t%.2f" %(val1, diff)
                y_array[1].append(diff)
            elif self._chart == 1:
                # chart processing for 2
                processed_data = "\t%.2f\t%.2f" %(val1, val2)
                y_array[1].append(val2)
            elif self._chart == 2:
                # chart processing for 3
                processed_data = "\t%.2f\t%.2f\t%.2f" %(val1, val2, val3)
                y_array[1].append(val2)
                y_array[2].append(val3)
            elif self._chart == 3:
                # chart processing for 4
                processed_data = "\t%.2f\t%.2f\t%.2f\t%.2f" %(val1, val2, val3, val4)
                y_array[1].append(val2)
                y_array[2].append(val3)
                y_array[3].append(val4)

            # confirmation in command line
            print round(recorded_time, 1), processed_data

            # publisher to send to update the timer
            self._conn.send("%d" %(round(recorded_time)))

            to_be_written = "\n%.2f%s" %(recorded_time, processed_data)

            # file I/O
            datafile = open(self._filename, "a")
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


    # sub-animation for each subsequent data point collected
    def animateSide(self, i, line, xdata, ydata, ax):
        if not self._continue:
            return
        
        # update plot
        line.set_data([xdata, ydata])
        # rescale the plots
        ax.relim()
        ax.autoscale_view()

        return line,




class MainFrame(gui.FrameMain):
    # for the initialization of the GUI
    def __init__(self, parent):
        gui.FrameMain.__init__(self, parent)

        print "Getting ready..."
        self.setStatus("Ready to go. Select Port to begin.")

        # initializing variables
        self.start_time = 0.0       # start time for referencing
        self.filename = ""          # filename for file I/O
        self.init_line = ""         # the first line of file to be reused
        self.initial_counter = 0    # the number of characters to be removed from the start of file
        self.ports = []             # list of ports of arduino for serial
        self.port = ""              # port for selection
        self.chart_num = 0          # charts that user want to display
        self.pause = True           # to decide whether acquisition stops
        self.arduino = ""           # arduino object
        self.worker = ""            # worker thread for updating voltage
        self.ani_worker = ""        # worker to run the animation
        self.timer_thread = ""      # timer thread
        self.parent_conn = ""       # parent_conn to child process

        # initialize the ports
        self.refresh()

        # create a pubsub receiver
        pub.subscribe(self.updateVoltage, "update_voltage")
        pub.subscribe(self.updateTimer, "update_timer")
        pub.subscribe(self.showMessage, "show_message")
        pub.subscribe(self.setStatus, "set_status")

    def updateVoltage(self, values):
        if len(values):
            x = "%.2f" %values[0]
            y = "%.2f" %values[1]
            z = "%.2f" %values[2]
            a = "%.2f" %values[3]

            if self.chart_num == 0:
                y = "%.2f" %(values[1] - values[2])

        else:
            x = "-"
            y = "-"
            z = "-"
            a = "-"

        self.xDisplay.SetValue(x)
        self.yDisplay.SetValue(y)
        self.zDisplay.SetValue(z)
        self.aDisplay.SetValue(a)

    def updateTimer(self, time):
        self.timerDisplay.SetValue(time)

    def showMessage(self, message):
        wx.MessageBox(message, "Note", 
            wx.OK | wx.ICON_INFORMATION)

    def setStatus(self, status):
        self.statusText.SetLabel(status)

    def selectPort(self, event=None):
        self.port = self.ports[self.portChoice.GetCurrentSelection()]

        # hide unused displays
        if self.chart_num < 3:
            self.aText.Hide()
            self.aDisplay.Hide()

        if self.chart_num < 2:
            self.zText.Hide()
            self.zDisplay.Hide()

        # kills all workers and restart port
        if self.worker:
            self.worker.abort()
            self.arduino.close()

        # setup serial b/w ard and python
        self.arduino = serial.Serial(self.port, 9600, timeout=1)

        self.worker = VoltageThread(self, self.arduino)
        self.worker.start()

        

    # selection of chart. if user selects chart (2 - 3), show the difference voltage
    def selectChart(self, event):
        self.chart_num = self.chartChoice.GetCurrentSelection()

        self.zText.Hide()
        self.zDisplay.Hide()
        self.aText.Hide()
        self.aDisplay.Hide()

        self.xText.Show()
        self.xDisplay.Show()
        self.yText.Show()
        self.yDisplay.Show()

        if self.chart_num > 1:
            self.zText.Show()
            self.zDisplay.Show()
        
        if self.chart_num > 2:
            self.aText.Show()
            self.aDisplay.Show()


    # check and update arduino ports
    def refresh(self, event=None):
        self.ports_selected = False

        # check if arduino port is available
        ports = list(list_ports.comports())

        self.portChoice.Clear()
        self.ports = []

        for p in ports:
            self.ports.append(p[0])
            self.portChoice.Append(p[1])

        # kill worker that updates the port
        if self.worker:
            self.worker.abort()

    # when user clicks the "Start" to begin acquistion
    def start(self, event):
        global port_configured

        # check if arduino port is available and selected. if not, cancel.
        if port_configured:
            print "Save file to begin data acquisition..."
            self.statusText.SetLabel("Save file to begin data acquisition.")

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
            self.showMessage("Port selected is not functioning or port is not selected. Select a functioning port to START.")
            return


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
        self.startButton.Disable()
        # disable port choice
        self.portChoice.Disable()
        # disable chart choice
        self.chartChoice.Disable()
        # disable all displays
        self.xDisplay.Disable()
        self.yDisplay.Disable()
        self.zDisplay.Disable()
        self.aDisplay.Disable()
        # enable end button
        self.endButton.Enable()
        # set timer to 0s
        self.timerDisplay.SetValue("0")


        # begin data acquisition
        # set variables
        self.chart_num = self.chartChoice.GetCurrentSelection()

        # kill the existing thread for updating the voltage values
        self.worker.abort()

        # process pipe
        self.parent_conn, child_conn = Pipe()

        # start animation process
        self.ani_worker = AnimationWorker(child_conn, self.port, self.chart_num, self.filename)
        self.ani_worker.start()

        # start timer thread
        self.timer_thread = TimerThread(self.parent_conn)
        self.timer_thread.start()

        self.statusText.SetLabel("Data acquisition started...")
       

    # when user clicks the end button
    def end(self, event):
        # stop timer thread
        self.timer_thread.abort()
        # end all animation
        if self.ani_worker.is_alive():
            self.parent_conn.send(1)
            self.parent_conn.recv()
            self.parent_conn.close()

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
        self.startButton.Enable()
        # enable chart picker
        self.portChoice.Enable()
        # enable chart picker
        self.chartChoice.Enable()
        # enable all displays
        self.xDisplay.Enable()
        self.yDisplay.Enable()
        self.zDisplay.Enable()
        self.aDisplay.Enable()
        # disable end button
        self.endButton.Disable()

        # restart worker to show voltage and difference
        print "Saving data and restarting arduino port..."
        self.selectPort(self)





if __name__ == "__main__":

    # initialize filename
    app = wx.App(False) 
    frame = MainFrame(None) 
    frame.Show(True) 
    #start the applications
    print "Application running... Do NOT close this window."
    app.MainLoop()