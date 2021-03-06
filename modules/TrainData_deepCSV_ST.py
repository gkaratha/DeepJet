'''
Created on 21 Feb 2017

@author: jkiesele
'''
from TrainData import TrainData_Flavour

import numpy


class TrainData_deepCSV_ST(TrainData_Flavour):
    '''
    same as TrainData_deepCSV but with 3 truth labels: UDSG C B
    '''


    def __init__(self):
        '''
        Constructor
        '''
        TrainData_Flavour.__init__(self)
        self.truthclasses=['isB','isC','isUDS','isG']
        
        self.addBranches(['jet_pt', 'jet_eta',
                           'TagVarCSV_jetNSecondaryVertices', 
                           'TagVarCSV_trackSumJetEtRatio', 'TagVarCSV_trackSumJetDeltaR', 
                           'TagVarCSV_vertexCategory', 'TagVarCSV_trackSip2dValAboveCharm', 
                           'TagVarCSV_trackSip2dSigAboveCharm', 'TagVarCSV_trackSip3dValAboveCharm', 
                           'TagVarCSV_trackSip3dSigAboveCharm', 'TagVarCSV_jetNSelectedTracks', 
                           'TagVarCSV_jetNTracksEtaRel'])
       
        self.addBranches(['TagVarCSVTrk_trackJetDistVal',
                              'TagVarCSVTrk_trackPtRel', 
                              'TagVarCSVTrk_trackDeltaR', 
                              'TagVarCSVTrk_trackPtRatio', 
                              'TagVarCSVTrk_trackSip3dSig', 
                              'TagVarCSVTrk_trackSip2dSig', 
                              'TagVarCSVTrk_trackDecayLenVal'],
                             6)
        
        
        self.addBranches(['TagVarCSV_trackEtaRel'],4)

        self.addBranches(['TagVarCSV_vertexMass', 
                              'TagVarCSV_vertexNTracks', 
                              'TagVarCSV_vertexEnergyRatio',
                              'TagVarCSV_vertexJetDeltaR',
                              'TagVarCSV_flightDistance2dVal', 
                              'TagVarCSV_flightDistance2dSig', 
                              'TagVarCSV_flightDistance3dVal', 
                              'TagVarCSV_flightDistance3dSig'],
                             1)


        self.reducedtruthclasses=['isB','isC','isUDSG']
        
    def reduceTruth(self, tuple_in):
        b = tuple_in['isB'].view(numpy.ndarray)
        c = tuple_in['isC'].view(numpy.ndarray)
        uds = tuple_in['isUDS'].view(numpy.ndarray)
        g = tuple_in['isG'].view(numpy.ndarray)
        l = g + uds
        self.reducedtruthclasses=['isB','isC','isUDSG']
        return numpy.vstack((b,c,l)).transpose()
        
        


class TrainData_deepCSV_ST_broad(TrainData_Flavour):
    '''
    same as TrainData_deepCSV but with 4 truth labels: UDS G C B
    '''


    def __init__(self):
        '''
        Constructor
        '''
        TrainData_Flavour.__init__(self)
        self.truthclasses=['isB','isC','isUDS','isG']
        
        self.addBranches(['jet_pt', 'jet_eta',
                           'TagVarCSV_jetNSecondaryVertices', 
                           'TagVarCSV_trackSumJetEtRatio', 'TagVarCSV_trackSumJetDeltaR', 
                           'TagVarCSV_vertexCategory', 'TagVarCSV_trackSip2dValAboveCharm', 
                           'TagVarCSV_trackSip2dSigAboveCharm', 'TagVarCSV_trackSip3dValAboveCharm', 
                           'TagVarCSV_trackSip3dSigAboveCharm', 'TagVarCSV_jetNSelectedTracks', 
                           'TagVarCSV_jetNTracksEtaRel'])
       
        self.addBranches(['TagVarCSVTrk_trackJetDistVal',
                              'TagVarCSVTrk_trackPtRel', 
                              'TagVarCSVTrk_trackDeltaR', 
                              'TagVarCSVTrk_trackPtRatio', 
                              'TagVarCSVTrk_trackSip3dSig', 
                              'TagVarCSVTrk_trackSip2dSig', 
                              'TagVarCSVTrk_trackDecayLenVal'],
                             10)
        
        
        self.addBranches(['TagVarCSV_trackEtaRel'],8)

        self.addBranches(['TagVarCSV_vertexMass', 
                              'TagVarCSV_vertexNTracks', 
                              'TagVarCSV_vertexEnergyRatio',
                              'TagVarCSV_vertexJetDeltaR',
                              'TagVarCSV_flightDistance2dVal', 
                              'TagVarCSV_flightDistance2dSig', 
                              'TagVarCSV_flightDistance3dVal', 
                              'TagVarCSV_flightDistance3dSig'],
                             5)


        self.reducedtruthclasses=['isB','isC','isUDSG']
        
    def reduceTruth(self, tuple_in):
        b = tuple_in['isB'].view(numpy.ndarray)
        c = tuple_in['isC'].view(numpy.ndarray)
        uds = tuple_in['isUDS'].view(numpy.ndarray)
        g = tuple_in['isG'].view(numpy.ndarray)
        l = g + uds
        self.reducedtruthclasses=['isB','isC','isUDSG']
        return numpy.vstack((b,c,l)).transpose()
        
        
      
      
