import serial
import time
import serial.tools.list_ports as list_ports
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

com = ""
chart_num = 2

# disable toolbar
#mpl.rcParams["toolbar"] = "None"

# check if arduino port is available
ports = list(list_ports.comports())
for p in ports:
    if "Arduino" in p[1]:
        print "Arduino detected!"
        com = p[0]
    else:
        print "No arduino found."


def animate1(i):
    arduino.write("1")
    # split data into arrays
    raw_data = arduino.readline().rstrip().split(",")
    processed_data = []
    
    # record time
    recorded_time = round((time.clock() - start), 4)

    # process data
    index = 0
    for data in raw_data:
        if (index < chart_num):
            new_data = round((float(data) / 1023.0 * 5.0), 4)
            processed_data.append(new_data)
            y_array[index].append(new_data)
        index += 1

    # confirmation in command line
    print round(recorded_time, 1), "\t", processed_data

    # file I/O

    # append to arrays
    xdata.append(recorded_time)
    
    y1line.set_data([xdata, y1data])

    ax1.relim()
    ax1.autoscale_view()

    return y1line,


def animate2(i):
    y2line.set_data([xdata, y2data])

    ax2.relim()
    ax2.autoscale_view()

    return y2line,

def animate3(i):
    y3line.set_data([xdata, y3data])

    ax3.relim()
    ax3.autoscale_view()

    return y3line,

def animate4(i):
    y4line.set_data([xdata, y4data])

    ax4.relim()
    ax4.autoscale_view()

    return y4line,



if com:
    time_interval = 960
    arduino = serial.Serial (com, 9600, timeout=1) #setup serial b/w ard and python

    print "Wait for a second for serial communication to initialize."
    time.sleep(1.5)   #delay 2s before commencement)

    xdata = []
    y1data = []
    y2data = []
    y3data = []
    y4data = []
    y_array = [y1data, y2data, y3data, y4data]

    # initialize figure 1
    fig1 = plt.figure()
    plt.title("Reading 1")
    plt.xlabel("Time (s)")
    plt.ylabel("Y (mV)")
    ax1 = plt.gca()

    ax1.relim()
    ax1.autoscale_view()

    y1line, = plt.plot([], [], "r-")

    ani1 = animation.FuncAnimation(fig1, animate1, interval=time_interval)

    if (chart_num > 1):
        # initialize figure 2
        fig2 = plt.figure()
        plt.title("Reading 2")
        plt.xlabel("Time (s)")
        plt.ylabel("Y (mV)")
        ax2 = plt.gca()

        ax2.relim()
        ax2.autoscale_view()

        y2line, = plt.plot([], [], "b-")
        ani2 = animation.FuncAnimation(fig2, animate2, interval=time_interval)

    if (chart_num > 2):
        # initialize figure 3
        fig3 = plt.figure()
        plt.title("Reading 3")
        plt.xlabel("Time (s)")
        plt.ylabel("Y (mV)")
        ax3 = plt.gca()

        ax3.relim()
        ax3.autoscale_view()

        y3line, = plt.plot([], [], "k-")
        ani3 = animation.FuncAnimation(fig3, animate3, interval=time_interval)
    
    if (chart_num > 3):
        # initialize figure 4
        fig4 = plt.figure()
        plt.title("Reading 4")
        plt.xlabel("Time (s)")
        plt.ylabel("Y (mV)")
        ax4 = plt.gca()

        ax4.relim()
        ax4.autoscale_view()

        y4line, = plt.plot([], [], "m-")
        ani4 = animation.FuncAnimation(fig4, animate4, interval=time_interval)


    print "Commence data acquisition."
    start = time.clock()

    plt.show()