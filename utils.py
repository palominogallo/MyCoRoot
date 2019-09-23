import ROOT as rt

def readObjects( filename, objectname ):
    tfile = rt.TFile(filename, "READ")
    htemp = tfile.Get(objectname )
    rt.SetOwnership(tfile, 0) # important to avoid errors
    return htemp
