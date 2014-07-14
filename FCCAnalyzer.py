from __future__ import division
import osgeo.ogr 
import sys

orleans_data = "../../google_drive/gis_database/united_states/by_state/louisiana/SUBREGIONS/orleans/scratch/orleans_fcc_and_HH_shape/orleans_ff_and_HH_I_v1.shp" 

class Analyzer:

  def generateTotal(self, featureIndex): 
    featureIndex = self.featureCount - 1
    total = 0
    while featureIndex > -1:
      feature = self.layer.GetFeature(featureIndex)
      total = total + feature.GetFieldAsInteger(self.field)
      featureIndex = featureIndex - 1
    return total

  def generateMean(self):
    return self.total/self.featureCount

  def generatePercent(self, mean):  
    mean = float(mean)
    numberArray = (str(mean)).split('.')  
    fractional = float('.' + numberArray[1])
    integral = int(self.returnFCCIntegral(numberArray[0]))
    dividend = integral + (fractional * 200)
    percentage = (dividend/1000) * 100
    return percentage 

  def returnFCCIntegral(self, FCCAverage):
    return {
      '0': 0,
      '1': 0,
      '2': 200,
      '3': 400,
      '4': 600,
      '5': 800 }[FCCAverage]


class DatasetAnalyzer(Analyzer):

  def __init__(self, dataset, field):
    dataset = osgeo.ogr.Open(dataset)
    self.field = field   
    self.layer = dataset.GetLayer(0)
    self.featureCount = self.layer.GetFeatureCount()
    self.total = self.generateTotal()
    self.mean = self.generateMean()
    self.percent = self.generatePercent(self.mean)


  
