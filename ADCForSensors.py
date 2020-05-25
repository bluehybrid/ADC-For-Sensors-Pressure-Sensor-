'''
Code for MCP3008 ADC using spidev Library to get the data from 
the ADC

int getADC(channel)
    -Intialize the ADC with the Channel that connected to the device 
     that you want to get data from it 
    -It gets the data and filtering it then Return the filtered Data 
    -Here there is 2 devices 
     Pressure Sensor Channel ----> 0
     Water Sensor Channel ----> 1
    -Example
    -----------
     while 1:
     print(getADC(0))
     sleep(0.1)
    ----------- 
'''
import spidev  

from time import sleep
def getADC(channel):

    if ((channel>7)or(channel<0)): #Checking if you choose a wrong channel
                                   #Note:Pressure Sensor Channel ----> 0 / Water Sensor Channel ----> 1
		return -1

    Spi = spidev.SpiDev() #Intializing SPI Communication

    Spi.open(0,0) #Open the bus and the device 

    retData = Spi.xfer([1,(8+channel)<<4,0])  #Sending 3 Bytes to the ADC and Recieving a list with 3 Bytes

    FData = ((retData[1]&3) << 8) + retData[2] #Filtering the returned data bytes from ADC and making the Data byte

    return FData  #Return the Data
