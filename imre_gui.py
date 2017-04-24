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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Everything Is Awesome!", pos = wx.DefaultPosition, size = wx.Size( 850,420 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        SizerFrame = wx.BoxSizer( wx.VERTICAL )
        
        self.MainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        SizerPanel = wx.BoxSizer( wx.VERTICAL )
        
        SizerPanel.SetMinSize( wx.Size( 850,-1 ) ) 
        self.filePicker1 = wx.FilePickerCtrl( self.MainPanel, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 850,-1 ), wx.FLP_DEFAULT_STYLE )
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
        
        chartChoiceChoices = [ u"2 - 3", u"2", u"3", u"4" ]
        self.chartChoice = wx.Choice( self.MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), chartChoiceChoices, 0 )
        self.chartChoice.SetSelection( 0 )
        SizerChart.Add( self.chartChoice, 0, wx.ALL, 5 )
        
        
        SizerTop.Add( SizerChart, 1, wx.EXPAND, 5 )
        
        SizerX = wx.BoxSizer( wx.VERTICAL )
        
        self.xText = wx.StaticText( self.MainPanel, wx.ID_ANY, u"X (mV)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.xText.Wrap( -1 )
        SizerX.Add( self.xText, 0, wx.ALL, 5 )
        
        self.xDisplay = wx.TextCtrl( self.MainPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
        self.xDisplay.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
        
        SizerX.Add( self.xDisplay, 0, wx.ALL, 5 )
        
        
        SizerTop.Add( SizerX, 1, wx.EXPAND, 5 )
        
        SizerY = wx.BoxSizer( wx.VERTICAL )
        
        self.yText = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Y (mV)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.yText.Wrap( -1 )
        SizerY.Add( self.yText, 0, wx.ALL, 5 )
        
        self.yDisplay = wx.TextCtrl( self.MainPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
        self.yDisplay.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        
        SizerY.Add( self.yDisplay, 0, wx.ALL, 5 )
        
        
        SizerTop.Add( SizerY, 1, wx.EXPAND, 5 )
        
        SizerZ = wx.BoxSizer( wx.VERTICAL )
        
        self.zText = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Z (mV)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.zText.Wrap( -1 )
        SizerZ.Add( self.zText, 0, wx.ALL, 5 )
        
        self.zDisplay = wx.TextCtrl( self.MainPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
        self.zDisplay.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        
        SizerZ.Add( self.zDisplay, 0, wx.ALL, 5 )
        
        
        SizerTop.Add( SizerZ, 1, wx.EXPAND, 5 )
        
        SizerA = wx.BoxSizer( wx.VERTICAL )
        
        self.aText = wx.StaticText( self.MainPanel, wx.ID_ANY, u"A (mV)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.aText.Wrap( -1 )
        SizerA.Add( self.aText, 0, wx.ALL, 5 )
        
        self.aDisplay = wx.TextCtrl( self.MainPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
        self.aDisplay.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        
        SizerA.Add( self.aDisplay, 0, wx.ALL, 5 )
        
        
        SizerTop.Add( SizerA, 1, wx.EXPAND, 5 )
        
        
        SizerPanel.Add( SizerTop, 1, wx.EXPAND, 5 )
        
        self.text2 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Remarks", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text2.Wrap( -1 )
        SizerPanel.Add( self.text2, 0, wx.ALL, 5 )
        
        self.input1 = wx.TextCtrl( self.MainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 850,-1 ), 0 )
        SizerPanel.Add( self.input1, 0, wx.ALL, 5 )
        
        self.input2 = wx.TextCtrl( self.MainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 850,-1 ), wx.TE_MULTILINE )
        SizerPanel.Add( self.input2, 0, wx.ALL, 5 )
        
        self.input3 = wx.TextCtrl( self.MainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 850,-1 ), 0 )
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
    

