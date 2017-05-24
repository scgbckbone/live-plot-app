import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

import matplotlib.animation as animation
from matplotlib import style
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib import pyplot as plt
import urllib
import json
import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None   # chain assignment exception from python

LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
style.use("ggplot")

f = plt.figure()   

exchange = "BTC-e"
DatCounter = 9000
programName = "btce"
resampleSize = "15Min"
DataPace = "tick"
candleWidth = 0.008
chartLoad = True
paneCount = 1

topIndicator = "none"
bottomIndicator = "none"
middleIndicator = "none"

darkColor = "#00A3E0"
lightColor = "#183A54"

EMAs = []
SMAs = []

def loadChart(run):
    global chartLoad
    if run == "start":
        chartLoad = True
    else:
        chartload = False

def tutorial():
    def page2():
        def page3():
            tut2.destroy()
            tut3 = tk.Tk()
            tut3.wm_title("Part 3!")
            label = ttk.Label(tut3, text="Part 3", font=NORMAL_FONT)
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(tut3, text="Done", command=tut3.destroy)
            B1.pack()
            tut3.mainloop()

        tut.destroy()
        tut2 = tk.Tk()
        tut2.wm_title("Part 2!")
        label = ttk.Label(tut2, text="Part 2", font=NORMAL_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(tut2, text="Next", command=page3)
        B1.pack()
        tut2.mainloop()

    tut = tk.Tk()
    tut.wm_title("Tutorial")
    label = ttk.Label(tut, text="What do you need help with", font=NORMAL_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(tut, text="Overview of the application", command=page2)
    B1.pack()
    B2 = ttk.Button(tut, text="How do I trade with this clients?", command=lambda: popupmsg("Not yet completed"))
    B2.pack()
    B3 = ttk.Button(tut, text="Indicators questions/help", command=lambda: popupmsg("Not yet completed"))
    B3.pack()
    tut.mainloop()



def addTopIndicator(what):
    global topIndicator
    global DatCounter

    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available")
    elif what == "none":
        topIndicator = what
        DatCounter = 9000
    elif what == "rsi":
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")
        label = ttk.Label(rsiQ, text="Choose how many periods you want each RSI calculation to consider.")
        label.pack(side="top", fill="x", pady=10)
        e = ttk.Entry(rsiQ)
        e.insert(0, 14)
        e.pack()
        e.focus_set()

        def callback():
            global topIndicator
            global DatCounter

            periods = (e.get())
            group = []
            group.append("rsi")
            group.append(periods)
            topIndicator = group
            DatCounter = 9000
            print("Set top indicator to", group)
            rsiQ.destroy()

        b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
        b.pack()
        tk.mainloop()

    elif what == "macd":
        global topIndicator
        global DatCounter

        topIndicator = "macd"
        DatCounter = 9000

def addMiddleIndicator(what):
    global middleIndicator
    global DatCounter

    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available")
    if what != "none":
        if middleIndicator == "none":
            if what == "sma":
                midIQ = tk.Tk()
                midIQ.wm_title("periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your SMA to be?")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middle indicator set to:", middleIndicator)
                    midIQ.destroy()
                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()

            if what == "ema":
                midIQ = tk.Tk()
                midIQ.wm_title("periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your SMA to be?")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middle indicator set to:", middleIndicator)
                    midIQ.destroy()
                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()

        else:
            if what == "sma":
                midIQ = tk.Tk()
                midIQ.wm_title("periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your SMA to be?")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    # middleIndicators = []
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middle indicator set to:", middleIndicator)
                    midIQ.destroy()
                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()

            if what == "ema":
                midIQ = tk.Tk()
                midIQ.wm_title("periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your SMA to be?")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    # middleIndicators = []
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middle indicator set to:", middleIndicator)
                    midIQ.destroy()
                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()

    else:
        middleIndicator = "none"



def addBottomIndicator(what):
        global bottomIndicator
        global DatCounter

        if DataPace == "tick":
            popupmsg("Indicators in Tick Data not available")
        elif what == "none":
            bottomIndicator = what
            DatCounter = 9000
        elif what == "rsi":
            rsiQ = tk.Tk()
            rsiQ.wm_title("Periods?")
            label = ttk.Label(rsiQ, text="Choose how many periods you want each RSI calculation to consider.")
            label.pack(side="top", fill="x", pady=10)
            e = ttk.Entry(rsiQ)
            e.insert(0, 14)
            e.pack()
            e.focus_set()

            def callback():
                global bottomIndicator
                global DatCounter

                periods = (e.get())
                group = []
                group.append("rsi")
                group.append(periods)
                bottomIndicator = group
                DatCounter = 9000
                print("Set bottom indicator to", group)
                rsiQ.destroy()

            b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
            b.pack()
            tk.mainloop()

        elif what == "macd":
            global bottomIndicator
            global DatCounter

            bottomIndicator = "macd"
            DatCounter = 9000

def changeTimeFrame(tf):
    global dataPace
    global DatCounter
    if tf == "7d" and resampleSize == "1Min":
        popupmsg("Too much data chosen, choose a smaller time frame or higher OHLC Interval")
    else:
        DataPace = tf
        DatCounter = 9000

def changeSampleSize(size, width):
    global resampleSize
    global DatCounter
    global candleWidth
    if DataPace == "7d" and size == "1Min":
        popupmsg("Too much data chosen, choose a smaller time frame or higher OHLC Interval.")
    elif DataPace == "tick":
        popupmsg("You're currently viewing tick data, not OHLC.")
    else:
        resampleSize = size
        DatCounter = 9000
        candleWidth = width

def changeExchange(towhat, pn):
    global exchange
    global DatCounter
    global programName

    exchange = towhat
    programName = pn
    DatCounter = 9000

def popupmsg(warning):
    popup = tk.Tk()
    popup.wm_title("!!!")
    label = ttk.Label(popup, text=warning, font=NORMAL_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()

def animate(i):
    global refreshRate
    global DatCounter

    if chartLoad:
        if paneCount == 1:
            if DataPace == "tick":
                try:
                    if exchange == "BTC-e":
                        a = plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)
                        a2 = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex=a)
                        dataLink = "https://btc-e.com/api/3/trades/btc_usd?limit=2000"
                        data = urllib.request.urlopen(dataLink)
                        data = data.read().decode("utf-8")
                        data = json.loads(data)
                        data = data["btc_usd"]
                        data = pd.DataFrame(data)
                        data["datestamp"] = np.array(data["timestamp"].astype("datetime64[s]"))
                        allDates = data["datestamp"].tolist()

                        buys = data[(data["type"] == "bid")]
                        # commented out because of previous three(-1) lines that were added
                        # buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
                        buyDates = (buys["datestamp"]).tolist()

                        sells = data[(data["type"] == "ask")]
                        # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
                        sellDates = (sells["datestamp"]).tolist()

                        volume = data["amount"]

                        a.clear()
                        a.plot_date(buyDates, buys["price"], lightColor, label="buys")
                        a.plot_date(sellDates, sells["price"], darkColor, label="sells")

                        a2.fill_between(allDates, 0, volume, facecolor=darkColor)
                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
                        plt.setp(a.get_xticklabels(), visible=False)

                        a.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), loc=3, ncol=2, borderaxespad=0)
                        title = "BTC-e BTCUSD Prices\nLast Price: {}$".format(str(data["price"][1999]))
                        a.set_title(title)

                    if exchange == "Bitstamp":
                        a = plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)
                        a2 = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex=a)
                        dataLink = "https://www.bitstamp.net/api/transactions/"
                        data = urllib.request.urlopen(dataLink)
                        data = data.read().decode("utf-8")
                        data = json.loads(data)
                        # data = data["btc_usd"]  # we do not need this - check the link
                        data = pd.DataFrame(data)
                        data["datestamp"] = np.array(data["date"].apply(int)).astype("datetime64[s]")
                        allDates = data["datestamp"].tolist()

                        # buys = data[(data["type"] == "bid")]
                        # # commented out because of previous three(-1) lines that were added
                        # # buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
                        # buyDates = (buys["datestamp"]).tolist()
                        #
                        # sells = data[(data["type"] == "ask")]
                        # # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
                        # sellDates = (sells["datestamp"]).tolist()

                        volume = data["amount"].apply(float).tolist()

                        a.clear()
                        a.plot_date(allDates, data["price"], lightColor, label="buys")
                        # a.plot_date(sellDates, sells["price"], darkColor, label="sells")

                        a2.fill_between(allDates, 0, volume, facecolor=darkColor)
                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
                        plt.setp(a.get_xticklabels(), visible=False)

                        a.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), loc=3, ncol=2, borderaxespad=0)
                        title = "Bitstamp BTCUSD Prices\nLast Price: {}$".format(str(data["price"][0]))
                        a.set_title(title)

                    if exchange == "Bitfinex":
                        a = plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)
                        a2 = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex=a)
                        dataLink = "https://api.bitfinex.com/v1/trades/btcusd?limit=2000"
                        data = urllib.request.urlopen(dataLink)
                        data = data.read().decode("utf-8")
                        data = json.loads(data)
                        data = pd.DataFrame(data)
                        data["datestamp"] = np.array(data["timestamp"].astype("datetime64[s]"))
                        allDates = data["datestamp"].tolist()

                        buys = data[(data["type"] == "buy")]
                        # commented out because of previous three(-1) lines that were added
                        # buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
                        buyDates = (buys["datestamp"]).tolist()

                        sells = data[(data["type"] == "sell")]
                        # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
                        sellDates = (sells["datestamp"]).tolist()

                        volume = data["amount"].apply(float).tolist()

                        a.clear()
                        a.plot_date(buyDates, buys["price"], lightColor, label="buys")
                        a.plot_date(sellDates, sells["price"], darkColor, label="sells")

                        a2.fill_between(allDates, 0, volume, facecolor=darkColor)
                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
                        plt.setp(a.get_xticklabels(), visible=False)

                        a.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), loc=3, ncol=2, borderaxespad=0)
                        title = "Bitfinex BTCUSD Prices\nLast Price: {}$".format(str(data["price"][0]))
                        a.set_title(title)

                except Exception as e:
                    print("Failed because of: ",e)

            else:
                if DatCounter > 12:
                    try:
                        if topIndicator != "none" and bottomIndicator != "none":
                            # main graph
                            a = plt.subplot2grid((6,4), (1,0), rownspan=3, colspan=4)
                            # Volume
                            a2 = plt.subplot2grid((6,4), (4,0), sharex=a, rowspan=1, colspan=4)
                            # bottom indicator
                            a3 = plt.subplot2grid((6,4), (5,0),sharex=a, rowspan=1, colspan=4)
                            # top indicator
                            a0 = plt.subplot2grid((6,4), (0,0), sharex=a, rowspan=1, colspan=4)

                        elif topIndicator != "none":
                            # main graph
                            a = plt.subplot2grid((6,4), (1,0), rownspan=4, colspan=4)
                            # Volume
                            a2 = plt.subplot2grid((6,4), (5,0), sharex=a, rowspan=1, colspan=4)
                            # top indicator
                            a0 = plt.subplot2grid((6,4), (0,0), sharex=a, rowspan=1, colspan=4)

                        elif bottomIndicator != "none":
                            # main graph
                            a = plt.subplot2grid((6,4), (0,0), rownspan=4, colspan=4)
                            # Volume
                            a2 = plt.subplot2grid((6,4), (4,0), sharex=a, rowspan=1, colspan=4)
                            # bottom indicator
                            a3 = plt.subplot2grid((6,4), (5,0),sharex=a, rowspan=1, colspan=4)
                        else:
                            # main graph
                            a = plt.subplot2grid((6,4), (0,0), rownspan=5, colspan=4)
                            # Volume
                            a2 = plt.subplot2grid((6,4), (5,0), sharex=a, rowspan=1, colspan=4)



                    except Exception as e:
                        print("failed in the non-tick animate: {}".format(str(e)))

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, "@/home/scag/Downloads/holahola-8.xbm") # has to be .xbm file - use bimp
        tk.Tk.wm_title(self, "Sea of BTC client")  # name of application

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command=lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        exchangeChoice = tk.Menu(menubar, tearoff=1)
        exchangeChoice.add_command(label="BTC-e", command=lambda: changeExchange("BTC-e","btce"))
        exchangeChoice.add_command(label="Bitfinex", command=lambda: changeExchange("Bitfinex","bitfinex"))
        exchangeChoice.add_command(label="Bitstamp", command=lambda: changeExchange("Bitstamp","bitstamp"))
        menubar.add_cascade(label="Exchange", menu=exchangeChoice)

        dataTF = tk.Menu(menubar, tearoff=1)
        dataTF.add_command(label="Tick", command=lambda: changeTimeFrame("tick"))
        dataTF.add_command(label="1 Day", command=lambda: changeTimeFrame("1d"))
        dataTF.add_command(label="3 Day", command=lambda: changeTimeFrame("3d"))
        dataTF.add_command(label="1 Week", command=lambda: changeTimeFrame("7d"))
        menubar.add_cascade(label="Data Time Frame", menu=dataTF)

        OHLCI = tk.Menu(menubar, tearoff=1)
        OHLCI.add_command(label="Tick", command=lambda: changeSampleSize("tick"))
        OHLCI.add_command(label="1 Minute", command=lambda: changeSampleSize("1Min", 0.0005))
        OHLCI.add_command(label="5 Minute", command=lambda: changeSampleSize("5Min", 0.003))
        OHLCI.add_command(label="15 Minute", command=lambda: changeSampleSize("15Min", 0.008))
        OHLCI.add_command(label="30 Minute", command=lambda: changeSampleSize("30Min", 0.016))
        OHLCI.add_command(label="1 Hour", command=lambda: changeSampleSize("1H", 0.032))
        OHLCI.add_command(label="3 Hour", command=lambda: changeSampleSize("3H", 0.096))
        menubar.add_cascade(label="OHLC Interval", menu=OHLCI)

        topIndi = tk.Menu(menubar, tearoff=1)
        topIndi.add_command(label="None", command=lambda: addTopIndicator("none"))
        topIndi.add_command(label="RSI", command=lambda: addTopIndicator("rsi"))
        topIndi.add_command(label="MACD", command=lambda: addTopIndicator("macd"))
        menubar.add_cascade(label="Top Indicator", menu=topIndi)

        mainIndi = tk.Menu(menubar, tearoff=1)
        mainIndi.add_command(label="None", command=lambda: addMiddleIndicator("none"))
        mainIndi.add_command(label="SMA", command=lambda: addMiddleIndicator("sma"))
        mainIndi.add_command(label="EMA", command=lambda: addMiddleIndicator("ema"))
        menubar.add_cascade(label="Main/middle Indicator", menu=mainIndi)

        bottomIndi = tk.Menu(menubar, tearoff=1)
        bottomIndi.add_command(label="None", command=lambda: addBottomIndicator("none"))
        bottomIndi.add_command(label="RSI", command=lambda: addBottomIndicator("rsi"))
        bottomIndi.add_command(label="MACD", command=lambda: addBottomIndicator("macd"))
        bottomIndi.add_cascade(label="Top Indicator", menu=bottomIndi)

        tradeButton = tk.Menu(menubar, tearoff=1)
        tradeButton.add_command(label="Manual Trading", command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_command(label="Automated Trading", command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_separator()
        tradeButton.add_command(label="Quick Buy", command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_command(label="Quick Sell", command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_separator()
        tradeButton.add_command(label="Set up Quick Buy/sell", command=lambda: popupmsg("This is not live yet"))
        menubar.add_cascade(label="Trading", menu=tradeButton)

        startStop = tk.Menu(menubar, tearoff=1)
        startStop.add_command(label="Resume", command=lambda: loadChart("start"))
        startStop.add_command(label="Pause", command=lambda: loadChart("stop"))
        menubar.add_cascade(label="Resume/Pause client", menu=startStop)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tutorial", command=tutorial)
        menubar.add_cascade(label="Help", menu=helpmenu)





        tk.Tk.config(self, menu=menubar)

        self.frames = {}
        for F in (StartPage, BTCe_Page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="No warrant of any bussines success", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Agree", command=lambda: controller.show_frame(BTCe_Page))
        button1.config(fg="red", bg="blue")
        button1.pack()
        button3 = ttk.Button(self, text="Disagree", command=quit)
        button3.pack()


class BTCe_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

app = SeaofBTCapp()
app.geometry("1280x720")
ani = animation.FuncAnimation(f, animate, interval=5000) # interval when you want to run the animate function again (in miliseconds)
app.mainloop()
