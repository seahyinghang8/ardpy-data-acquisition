# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 21 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FrameMain
###########################################################################

class FrameMain ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Everything Is Awesome!", pos = wx.DefaultPosition, size = wx.Size( 750,357 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        SizerFrame = wx.BoxSizer( wx.VERTICAL )
        
        self.MainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        SizerPanel = wx.BoxSizer( wx.VERTICAL )
        
        SizerPanel.SetMinSize( wx.Size( 800,-1 ) ) 
        self.filePicker1 = wx.FilePickerCtrl( self.MainPanel, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 800,-1 ), wx.FLP_DEFAULT_STYLE )
        self.filePicker1.Enable( False )
        
        SizerPanel.Add( self.filePicker1, 0, wx.ALL, 5 )
        
        SizerTop = wx.BoxSizer( wx.HORIZONTAL )
        
        SizerPort = wx.BoxSizer( wx.VERTICAL )
        
        self.text7 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text7.Wrap( -1 )
        SizerPort.Add( self.text7, 0, wx.ALL, 5 )
        
        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
        
        portChoiceChoices = [ wx.EmptyString ]
        self.portChoice = wx.Choice( self.MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, portChoiceChoices, 0 )
        self.portChoice.SetSelection( 0 )
        self.portChoice.SetMinSize( wx.Size( 100,-1 ) )
        
        bSizer12.Add( self.portChoice, 0, wx.ALL, 5 )
        
        self.refreshButton = wx.BitmapButton( self.MainPanel, wx.ID_ANY, wx.Bitmap( u"resource/refresh.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
        bSizer12.Add( self.refreshButton, 0, wx.ALL, 5 )
        
        
        SizerPort.Add( bSizer12, 1, wx.EXPAND, 5 )
        
        
        SizerTop.Add( SizerPort, 1, wx.EXPAND, 5 )
        
        SizerChart = wx.BoxSizer( wx.VERTICAL )
        
        self.text3 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Type of Charts", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text3.Wrap( -1 )
        SizerChart.Add( self.text3, 0, wx.ALL, 5 )
        
        chartChoiceChoices = [ u"2 - 3", u"3", u"2" ]
        self.chartChoice = wx.Choice( self.MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), chartChoiceChoices, 0 )
        self.chartChoice.SetSelection( 0 )
        SizerChart.Add( self.chartChoice, 0, wx.ALL, 5 )
        
        
        SizerTop.Add( SizerChart, 1, wx.EXPAND, 5 )
        
        SizerVoltage = wx.BoxSizer( wx.VERTICAL )
        
        self.text4 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Voltage (mV)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text4.Wrap( -1 )
        SizerVoltage.Add( self.text4, 0, wx.ALL, 5 )
        
        self.voltageDisplay = wx.TextCtrl( self.MainPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
        self.voltageDisplay.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
        
        SizerVoltage.Add( self.voltageDisplay, 0, wx.ALL, 5 )
        
        
        SizerTop.Add( SizerVoltage, 1, wx.EXPAND, 5 )
        
        SizerScale = wx.BoxSizer( wx.VERTICAL )
        
        self.text6 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Difference (mV)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text6.Wrap( -1 )
        SizerScale.Add( self.text6, 0, wx.ALL, 5 )
        
        self.differenceDisplay = wx.TextCtrl( self.MainPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
        self.differenceDisplay.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        
        SizerScale.Add( self.differenceDisplay, 0, wx.ALL, 5 )
        
        
        SizerTop.Add( SizerScale, 1, wx.EXPAND, 5 )
        
        
        SizerPanel.Add( SizerTop, 1, wx.EXPAND, 5 )
        
        self.text2 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Remarks", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text2.Wrap( -1 )
        SizerPanel.Add( self.text2, 0, wx.ALL, 5 )
        
        self.input1 = wx.TextCtrl( self.MainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 800,-1 ), 0 )
        SizerPanel.Add( self.input1, 0, wx.ALL, 5 )
        
        self.input2 = wx.TextCtrl( self.MainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 800,-1 ), wx.TE_MULTILINE )
        SizerPanel.Add( self.input2, 0, wx.ALL, 5 )
        
        self.input3 = wx.TextCtrl( self.MainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 800,-1 ), 0 )
        SizerPanel.Add( self.input3, 0, wx.ALL, 5 )
        
        SizerBottomMain = wx.BoxSizer( wx.HORIZONTAL )
        
        SizerBottom2 = wx.BoxSizer( wx.VERTICAL )
        
        SizerButton = wx.BoxSizer( wx.HORIZONTAL )
        
        self.startButton = wx.Button( self.MainPanel, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        SizerButton.Add( self.startButton, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
        
        self.endButton = wx.Button( self.MainPanel, wx.ID_ANY, u"End", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.endButton.Enable( False )
        
        SizerButton.Add( self.endButton, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
        
        
        SizerBottom2.Add( SizerButton, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        SizerBottomMain.Add( SizerBottom2, 1, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
        
        SizerTimer = wx.BoxSizer( wx.VERTICAL )
        
        self.text4 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Timer (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text4.Wrap( -1 )
        SizerTimer.Add( self.text4, 0, wx.ALL, 5 )
        
        self.timerDisplay = wx.TextCtrl( self.MainPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
        self.timerDisplay.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        
        SizerTimer.Add( self.timerDisplay, 0, wx.ALL, 5 )
        
        
        SizerBottomMain.Add( SizerTimer, 1, wx.ALIGN_BOTTOM, 30 )
        
        SizerStatus = wx.BoxSizer( wx.HORIZONTAL )
        
        self.statusText = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Starting Up...", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.statusText.Wrap( -1 )
        self.statusText.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        
        SizerStatus.Add( self.statusText, 0, wx.ALL, 5 )
        
        
        SizerBottomMain.Add( SizerStatus, 1, wx.ALIGN_BOTTOM, 5 )
        
        
        SizerPanel.Add( SizerBottomMain, 1, wx.EXPAND, 5 )
        
        
        self.MainPanel.SetSizer( SizerPanel )
        self.MainPanel.Layout()
        SizerPanel.Fit( self.MainPanel )
        SizerFrame.Add( self.MainPanel, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( SizerFrame )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.portChoice.Bind( wx.EVT_CHOICE, self.selectPort )
        self.refreshButton.Bind( wx.EVT_BUTTON, self.refresh )
        self.chartChoice.Bind( wx.EVT_CHOICE, self.selectChart )
        self.startButton.Bind( wx.EVT_BUTTON, self.start )
        self.endButton.Bind( wx.EVT_BUTTON, self.end )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def selectPort( self, event ):
        event.Skip()
    
    def refresh( self, event ):
        event.Skip()
    
    def selectChart( self, event ):
        event.Skip()
    
    def start( self, event ):
        event.Skip()
    
    def end( self, event ):
        event.Skip()
    

