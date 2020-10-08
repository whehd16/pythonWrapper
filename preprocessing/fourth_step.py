import pandas as pd

#특징선택 이후 csv 편
def makeArff(kospiCSV, f):
    target = 'KOSPI'
    f.write('@relation ' + target + '\n')

    for column in kospiCSV.columns:
        f.write('@attribute ' + column)
        if (column == 'Date'):
            f.write(' date yyyy-MM-dd\n')
        else:
            f.write(' numeric\n')

    f.write('\n@data\n')

    rows = len(kospiCSV)
    for row in range(rows):
        # print(row)
        try:
            for column in kospiCSV.columns:
                f.write(str(kospiCSV.loc[row][column]))
                if (column != kospiCSV.columns[len(kospiCSV.columns) - 1]):
                    f.write(', ')
                else:
                    f.write('\n')

        except:
            f.close()

def deleteFeatures(csv_path, delete_list, f):
    csv = pd.read_csv(csv_path)
    csv = csv.drop([csv.columns[i-1] for i in delete_list], 1)
    makeArff(csv, f)


# train csv 랑 test csv 모두 특징 지워서 arff 로 만들어보기!
#지수 unused
index_2007_2008 = [3,8,11,13,16,18,22,27,28,30,32,34,36,40,41,44,52,56,58,59,60,65,66,68,69,71,73,77,78,79,81,83,84,85,88,90,92,93,96,98,101,104,105,106,108,112,113,118,119,120,121,124,126,127,130,132,134,136,137,138,139,142,144,148,150,151,160,164,167,169,171,180,182,185,187,191,192,194,195,198,199,200,207,209,217,219,220,221,228,230,231,232,233,240,243,246,250,251,255,258,259,261,264,265,266] #106개 unused
index_2009_2010 = [6,8,11,14,18,20,21,23,24,26,27,31,33,37,43,45,50,54,58,61,68,72,81,83,84,85,88,90,96,101,105,106,107,111,112,115,118,119,121,123,125,126,133,136,137,138,139,142,143,146,147,151,152,154,155,156,158,160,164,165,169,170,171,172,174,176,183,184,185,186,187,190,191,194,195,200,204,208,212,216,217,218,220,221,223,224,226,230,231,232,235,241,242,243,246,247,249,252,253,254,259,261,262,263,265] #106개 unused
index_2011_2012 = [4,5,6,7,9,10,11,13,14,15,18,22,24,25,32,36,37,39,40,41,42,43,45,46,47,48,50,51,52,56,57,59,60,65,67,69,70,71,73,76,80,83,85,86,88,89,91,92,95,100,106,110,111,113,114,115,116,117,119,120,123,126,128,130,135,138,139,140,142,144,150,152,153,154,156,157,158,160,163,164,165,166,167,169,170,173,174,175,176,180,181,183,185,190,191,192,199,200,202,205,209,210,211,214,215,217,220,222,225,229,234,235,237,242,243,244,246,248,249,252,253,254,255,257,261,262,263,266]
index_2013_2014 = [3,4,9,10,16,18,19,23,25,28,30,40,42,44,45,46,49,50,51,52,54,55,56,59,61,63,66,67,71,75,78,81,82,84,85,86,93,97,98,99,103,104,105,106,107,109,111,112,113,117,118,120,121,124,126,131,132,134,137,139,140,141,147,148,149,150,153,155,156,157,158,159,160,163,168,171,172,175,177,180,183,184,191,194,199,203,210,212,213,215,217,218,220,226,227,228,229,230,231,232,234,235,239,241,242,245,246,247,248,250,251,253,254,255,260,261,262,264,265,266] #122 unused
index_2015_2016 = [7,9,10,15,16,19,20,22,24,25,27,29,30,31,37,38,40,45,50,52,56,58,61,65,66,69,70,71,72,81,83,84,85,87,88,92,93,94,95,97,99,100,104,107,111,112,117,118,120,121,124,126,130,131,132,133,134,135,136,139,140,142,146,147,149,152,155,157,158,159,160,166,169,170,172,176,177,179,181,182,183,185,189,190,193,194,196,202,203,205,207,208,215,218,219,221,222,223,226,227,228,229,231,232,235,236,245,248,250,251,252,253,254,256,257,258,259,260,261,262] #122 unused

index_2007_2009 = [3,4,5,11,15,16,19,21,22,23,26,28,30,31,35,37,40,42,43,52,58,62,63,64,66,75,83,84,86,88,91,96,97,101,103,105,106,107,108,111,113,116,121,122,129,130,137,138,141,144,147,148,152,153,154,158,160,161,165,167,168,169,170,172,174,175,176,177,179,181,190,191,193,194,195,197,199,203,204,206,207,208,210,211,212,213,214,215,219,225,230,232,234,238,239,240,244,246,250,252,253,255,256,257,260,262,264,265] #109 unused
index_2009_2011 = [4,6,12,16,18,21,24,25,26,27,28,30,32,41,43,44,48,53,55,56,57,60,61,63,65,67,68,73,74,75,79,80,81,84,85,88,89,94,95,97,101,105,106,108,111,112,114,116,118,119,121,123,124,125,126,136,140,141,142,144,145,147,151,152,153,156,157,159,160,161,165,166,169,172,173,174,175,187,188,191,194,196,202,203,206,207,208,209,211,212,217,218,219,225,227,228,234,235,236,239,244,246,247,249,250,255,258,259,260,266]#111 unused
index_2011_2013 = [3,4,5,9,10,22,26,29,31,32,34,36,39,43,44,45,47,49,50,53,57,58,59,61,62,67,68,70,71,75,79,80,81,82,84,86,90,93,95,96,97,98,99,100,104,107,109,112,113,114,117,118,119,123,125,126,128,130,131,132,133,139,140,143,144,145,146,149,151,156,157,159,160,163,164,167,169,172,173,178,179,180,181,184,185,186,190,191,192,193,194, 202,203,204,208,210,211,216,217,219,220,224,226,228,230,232,234,235,236,237,238,239,241,242,243,244,245,250,252,253,254,256,257,258,263,264,266] #128 unused
index_2013_2015 = [5,6,7,9,10,11,13,14,15,16,17,18,19,23,24,25,28,29,30,31,33,35,37,42,44,47,48,51,53,60,63,64,70,71,74,77,79,81,82,84,86,88,93,94,95,96,98,105,107,108,113,117,122,125,126,127,128,129,130,133,134,137,138,139,142,144,145,148,150,154,155,156,157,158,159,161,164,165,168,174,175,177,180,181,182,184,185,187,188,189,190,193,199,201,203,209,211,214,215,216,219,221,224,225,230,232,236,237,239,240,243,244,245,246,247,251,256,260,262,263,264]
index_2015_2017 = [3,4,12,13,15,16,17,18,19,28,30,34,38,39,40,45,47,52,53,54,56,62,63,64,69,72,73,75,84,89,91,96,97,100,101,102,103,110,113,114,115,116,120,124,125,126,127,134,135,136,140,142,152,153,154,155,157,161,164,165,167,170,172,174,176,181,187,188,191,195,196,197,200,205,206,207,210,211,213,214,221,223,225,228,229,232,235,236,237,243,246,248,251,253,258,259,260,265,266]

index_2010_2012 = [4,5,8,12,13,14,16,17,18,19,21,22,28,29,30,32,34,35,37,39,40,41,42,43,45,48,49,51,52,54,58,65,70,72,75,78,79,80,81,83,85,87,89,90,95,101,102,105,107,108,113,117,118,119,123,124,129,135,136,137,138,139,141,144,145,147,149,151,155,157,158,159,160,161,162,163,166,173,174,184,189,191,192,195,196,198,199,202,205,206,209,210,211,213,214,217,218,226,227,230,231,234,235,236,241,243,245,246,247,248,250,253,254,257,260,261,263,265]

index_2007_2010 = [4,8,15,17,18,20,21,22,27,28,29,30,33,34,37,39,40,43,45,51,55,56,59,66,70,78,83,86,87,90,91,92,93,96,97,99,102,105,106,107,114,118,119,129,131,136,139,140,141,142,144,146,149,152,153,158,161,162,165,166,168,170,172,173,174,175,181,183,185,186,188,191,192,193,194,200,202,209,210,211,214,216,219,220,221,222,223,224,227,228,229,230,245,246,247,248,255,257,259,260,261,263,266] #105 unused
index_2010_2013 = [5,9,10,11,14,16,19,20,21,24,26,28,32,33,34,36,41,42,43,44,48,49,52,53,54,55,58,59,60,65,66,70,73,79,81,82,84,86,91,95,100,101,102,103,105,107,108,112,114,115,117,118,121,122,123,125,128,130,133,134,137,139, 145,146,148,150,152,153,155,158,161,165,167,168,169,172,176,177,181,184,186,188,189,192,197,206,207,210,211,212,216,218,221,222,223,228,235,236,240,247,248,249,252,253,255,258,259,260,263,264,265]
index_2013_2016 = [7, 9, 10, 13, 14, 15, 16, 18, 19, 25, 28, 29, 32, 34, 35, 38, 39, 41, 42, 44, 47, 48, 49, 50, 53, 55, 56, 58, 59, 60,62,63,64,65,66,69,70,71,72,73,74,75,76,77,80,82,84,85,86,87,88,89,90,91,95,98,106,108,109,110,113,117,118,119,120,123,124,125,126,128,129,130,133,134,135,137,138,139,143,144,145,148,150,151,156,159,160,161,164,166,167,168,170,172,174,179,183,185,186,187,]

index_2011_2014 = [3,4,12,13,20,25,26,30,31,32,33,43,47,48,50,52,56,57,58,60,61,64,65,71,73,77,78,79,81,84,85,88,93,94,95,96,102,103,105,106,113,114,115,116,118,119,122,123,127,128,130,131,132,136,137,138,141,145,147,148,149,151,152,153,155,156,160,161,162,163,164,166,169,172,177,179,180,181,182,183,184,188,190,192,195,198,199,200,202,205,206,209,211,212,213,214,216,217,218,226,227,231,232,233,234,237,238,239,241,242,245,247,251,252,253,254,256,261]

index_2007_2011 = [4,9,15,16,17,18,19,20,21,24,31,39,44,45,51,62,65,66,70,80,82,84,86,95,98,99,100,104,108,109,110,111,112,118,119,121,123,124,125,126,139,144,153,157,159,161,164,168,171,172,176,177,178,179,182,183,189,196,199,200,201,202,203,204,212,213,216,217,223,225,226,228,230,241,243,244,245,246,247,248,249,252,253,255,257,258,259,260,261,264,266]
index_2011_2015 = [3, 4, 7, 8, 9, 11, 12, 13, 15, 17, 19, 23, 24, 25, 28, 29, 30, 32, 33, 34, 36, 39, 40, 46, 49, 56, 58, 62, 64, 69, 70, 72, 73, 75, 76, 81, 92, 93, 100, 101, 103, 105, 109, 111, 112, 113, 115, 118, 119, 121, 128, 130, 131, 133, 135, 138, 139, 144, 145, 146, 149, 150, 151, 152, 155, 158, 159, 160, 163, 164, 165, 167, 170, 172, 173, 174, 176, 178, 180, 181,184,185,189,191,192,193,197,198,199,201,203,209,214,217,219,221,222,223,227,228,229,232,236,239,240,242,245,246,249,250,251,255,258,260,261,263,264,265
]

####################
#변화량
delta_2007_2008 = [5,6,7,14,16,19,20,21,26,28,32,33,35,36,37,38,41,42,45,46,49,50,51,53,54,55,56,57,60,61,62,63,66,67,72,73,75,80,83,85,89,92,93,94,97,99,104,105,109,110,112,114,115,116,117,119,120,121,122,123,129,130,133,141,142,144,146,148,149,150,152,154,158,159,160,162,164,165,169,171,172,173,174,175,176,179,183,185,186,188,189,192,193,195,198,199,200,201,204,206,209,210,211,212,213,215,216,222,224,225,227,231,232,233,235,237,239,240,241,243,44,245,248,249,253,254,255,260,261,262,263,266]
delta_2009_2010 = [3,4,5,8,9,12,13,14,15,16,17,19,22,23,26,28,29,31,33,38,41,42,44,48,50,51,54,55,58,59,61,62,63,64,65,70,71,72,73,75,76,77,78,79,81,82,84,85,86,87,88,89,90,92,93,94,96,97,99,100,102,103,104,105,110,112,114,115,117,118,119,120,121,122,127,128,130,132,133,134,139,140,141,142,145,146,148,149,150,151,153,154,155,156,157,159,161,162,163,164,165,169,171,173,175,176,178,179,181,182,183,186,187,188,189,192,199,201,202,204,205,207,210,213,214,216,219,221,222,223,227,228,229,230,231,233,234,236,238,240,242,244,247,248,254,255,256,257,259,265,266]
delta_2011_2012 = [3,4,5,7,8,9,11,15,16,17,18,21,22,23,25,26,28,32,33,35,37,38,39,41,45,46,48,50,53,54,61,63,64,65,66,67,71,73,75,76,81,84,86,87,89,91,92,94,95,97,99,100,102,103,105,106,108,113,114,116,118,119,120,122,123,125,126,127,132,137,139,140,142,147,148,149,150,152,153,156,157,161,164,165,167,168,169,170,172,174,176,177,180,184,187,191,192,194,196,197,199,200,206,207,209,211,212,213,214,216,218,219,224,226,229,232,241,242,243,244,245,246,248,249,252,253,255,258,262,263,264]
delta_2013_2014 = [5,6,7,8,9,12,14,16,20,21,22,23,24,26,27,28,32,33,36,37,39,40,41,43,44,46,48,50,52,54,55,57,58,60,61,62,63,64,65,66,67,68,70,73,74,75,76,78,84,89,90,93,94,95,96,99,100,102,103,106,108,110,112,114,115,117,118,122,123,124,125,127,130,131,133,134,135,137,138,139,142,144,145,146,147,150,153,154,155,156,158,159,162,163,164,165,167,169,170,172,173,174,175,180,181,183,186,189,190,191,197,200,201,202,206,208,209,211,213,218,222,223,226,229,230,234,236,238,240,241,243,247,248,249,250,251,252,253,254,255,256,258,259,260,262,263,264,266]
delta_2015_2016 = [3,4,6,11,12,13,15,16,17,18,19,20,22,25,26,27,30,32,35,37,38,41,43,46,49,51,54,55,57,61,62,63,71,74,77,78,79,80,83,84,85,86,87,89,91,92,98,99,101,103,104,106,107,108,111,113,117,118,119,122,127,129,132,134,136,138,139,140,142,143,144,145,146,147,152,155,157,159,160,161,166,168,169,172,173,175,176,178,180,182,184,191,192,194,196,199,200,201,202,204,205,206,207,209,210,212,215,217,218,221,222,223,224,225,229,230,231,233,234,236,237,240,244,245,246,247,254,255,259,260,266]

delta_2007_2009 = [5,6,9,11,12,13,14,16,18,20,21,26,27,28,29,30,31,33,35,36,39,40,42,43,45,49,51,52,53,54,57,58,62,66,70,72,73,74,76,78,81,82,85,89,91,93,94,95,96,97,98,99,100,101,102,103,105,106,109,110,111,112,113,116,118,119,121,126,127,129,131,133,134,135,138,139,140,142,144,145,148,149,151,154,157,158,160,163,166,168,169,172,173,174,176,177,178,181,183,185,187,188,189,190,191,192,197,200,201,202,203,205,209,210,214,217,220,221,223,228,229,230,232,235,237,238,239,240,241,243,245,247,250,252,253,257,258,261,263,265]
delta_2009_2011 = [5,6,9,11,12,13,14,16,18,20,21,26,27,28,29,30,31,33,35,36,39,40,42,43,45,49,51,52,53,54,57,58,62,66,70,72,73,74,76,78,81,82,85,89,91,94,95,96,97,98,99,100,101,102,103,105,106,109,110,111,112,113,116,118,119,121,126,127,129,131,133,134,135,138,139,140,142,144,145,148,149,151,154,157,158,160,163,166,168,169,172,173,174,176,177,178,181,183,185,187,188,189,190,191,192,197,200,201,202,203,205,209,210,214,217,220,221,223,228,229,230,232,235,237,238,239,240,241,243,245,247,250,252,253,257,258,261,263,265]
delta_2011_2013 = [7,8,9,11,12,13,14,16,21,24,27,29,31,32,33,36,37,39,40,41,42,43,44,48,49,52,57,58,59,63,65,66,67,68,69,73,76,79,80,81,83,86,87,89,90,91,93,94,95,97,98,99,100,101,102,104,108,111,112,113,114,121,123,124,125,127,128,129,130,134,135,137,138,140,142,145,146,148,149,152,153,155,156,157,159,165,167,169,175,176,177,179,181,185,186,188,189,190,191,192,193,195,199,200,201,203,204,205,206,208,211,212,217,220,222,226,228,229,231,234,237,238,239,242,244,246,247,248,249,250,252,253,255,256,257,260,261,262,264,266]
delta_2013_2015 = [3,4,6,7,9,10,11,12,15,16,18,19,21,23,24,27,29,30,31,32,38,40,41,43,44,45,46,47,50,51,54,55,57,59,61,63,64,65,68,69,70,71,73,74,77,78,79,81,82,83,85,86,89,90,91,92,93,94,98,102,104,106,108,109,111,112,113,115,117,119,120,121,122,123,124,125,127,128,129,130,131,132,134,139,140,141,143,144,146,149,150,153,155,156,157,158,161,164,165,168,169,170,173,175,176,178,179,182,183,185,187,188,189,190,192,193,194,195,201,202,205,206,210,211,212,215,219,222,223,224,226,227,229,230,231,233,234,241,242,243,246,247,248,249,251,257,259,260,264,265,266]
delta_2015_2017 = [3,7,8,10,11,13,15,16,17,18,19,20,21,23,25,26,28,30,34,38,39,45,52,55,57,58,59,62,64,65,67,68,73,74,76,79,83,85,89,91,95,99,100,101,102,103,104,106,107,116,118,119,121,123,125,126,128,132,134,138,140,146,148,149,150,152,153,158,160,161,164,165,166,168,171,174,175,176,182,184,185,186,187,188,189,192,197,198,204,206,207,208,209,214,216,217,219,220,221,223,224,225,229,231,232,233,234,235,236,237,239,242,243,246,247,248,249,250,251,252,255,256,257,261,262,264,265,266]

delta_2010_2012 = [3,6,7,8,10,12,13,15,17,18,19,20,23,25,26,27,30,32,33,34,35,36,37,38,39,40,41,42,43,46,50,54,55,56,58,61,65,67,68,70,71,72,73,74,79,83,84,88,91,92,94,95,97,99,101,104,105,108,111,114,116,117,118,120,122,124,125,126,127,129,132,133,134,135,137,138,140,143,144,145,147,149,151,154,156,160,163,167,168,169,172,173,174,175,179,180,181,182,184,185,188,189,194,196,197,198,199,201,202,203,204,205,208,209,210,211,216,219,220,222,223,224,227,229,236,237,238,240,242,243,247,248,249,250,252,254,256,258,261,263]

delta_2007_2010 = [10,11,14,16,17,19,20,21,22,25,28,29,31,33,35,36,38,40,43,44,47,48,49,51,54,55,56,57,58,63,64,65,70,73,74,76,77,78,80,82,86,87,90,92,93,94,95,96,97,98,101,103,104,106,107,108,109,111,112,115,116,121,122,128,129,130,133,134,135,137,138,139,140,141,142,143,146,152,153,155,158,161,162,165,168,169,171,172,173,175,176,177,178,181,182,183,192,193,194,195,198,199,200,201,203,207,208,210,213,214,217,218,219,221,222,223,224,229,230,234,235,240,242,248,250,251,253,254,255,258,260,261,262,264,265,266]
delta_2010_2013 = [3,4,5,10,11,13,16,17,18,19,20,27,30,31,32,34,37,38,39,41,43,44,45,46,47,48,49,51,54,55,56,57,58,59,60,61,64,70,71,72,76,77,78,80,81,83,88,89,90,100,102,103,109,110,112,113,115,118,119,121,123,124,125,126,130,131,132,134,135,140,141,142,143,145,146,147,148,152,155,159,161,162,165,169,170,174,177,179,180,181,182,183,184,186,188,190,193,195,196,197,198,202,203,206,207,209,210,211,212,216,217,218,220,221,222,223,224,225,231,234,237,244,245,247,252,254,255,256,265,266]
delta_2013_2016 = [3,4,7,8,11,13,17,18,19,20,21,25,26,27,30,34,38,39,40,43,44,45,46,48,50,52,55,57,60,61,62,65,67,69,70,72,73,74,76,77,79,80,81,82,83,86,87,88,89,91,92,93,95,96,100,103,104,106,110,111,112,116,117,118,119,120,122,123,127,128,130,134,137,138,141,142,144,145,146,147,148,149,150,154,155,156,157,158,159,161,162,170,171,176,177,179,180,182,184,189,191,199,202,204,205,206,207,209,211,212,213,215,216,218,219,220,221,224,225,226,229,230,236,237,240,243,250,251,256,257,259,260,261,262,263,264,265]

delta_2011_2014 = [3,5,9,10,11,13,14,15,16,17,18,19,21,23,26,27,28,30,34,38,41,43,44,46,53,56,57,60,62,65,67,68,71,72,73,76,77,79,80,81,84,85,86,87,88,89,90,92,93,97,99,101,102,103,104,105,106,107,109,114,115,116,117,119,120,121,122,125,127,128,129,130,132,133,134,135,137,138,139,140,142,148,152,155,156,157,158,159,162,165,166,170,171,172,173,174,176,180,181,182,183,184,185,187,191,193,195,196,198,200,201,202,203,207,209,213,218,219,223,228,231,232,238,239,240,242,243,244,245,246,247,248,250,251,252,253,254,256,258,260,261,263,264,266]

delta_2007_2011 = [3,5,6,9,14,15,17,22,23,26,30,31,33,38,39,40,43,45,46,47,48,49,52,53,56,57,60,63,65,67,70,72,74,79,86,87,88,89,90,92,96,99,101,102,104,105,108,110,115,116,118,121,123,125,126,129,132,133,134,137,141,147,151,155,157,158,159,161,162,163,164,168,169,173,174,175,176,177,178,180,181,184,185,186,189,193,194,197,198,199,202,207,210,213,215,218,221,224,225,226,227,229,233,237,238,242,244,245,246,248,250,256,260,262,263]
delta_2011_2015 = [4,6,9,11,12,13,14,15,20,21,27,28,29,33,35,36,37,38,39,40,43,45,49,51,52,58,59,63,64,65,67,68,69,70,74,76,80,82,83,85,89,90,92,94,95,97,98,99,102,105,106,112,113,114,116,121,124,126,127,128,129,131,137,138,140,141,143,144,145,148,150,151,152,153,154,155,156,157,162,168,175,178,183,185,191,192,193,194,196,197,199,201,204,205,206,210,212,214,219,222,229,234,235,237,238,239,240,242,245,246,247,248,250,254,257,262,264,265]


rate_2013_2014 = [7, 9, 10, 11, 12, 14, 15, 16, 20, 21, 23, 25, 26, 27, 31, 32, 35, 37, 41, 43, 45, 46, 47, 48, 50, 51, 52, 53, 55, 56, 57, 59, 61, 62, 63, 65, 67, 69, 71, 73, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 90, 91, 93, 95, 98, 100, 101, 102, 103, 107, 109, 112, 113, 115, 116, 118, 120, 123, 124, 125, 126, 129, 133, 134, 135, 137, 138, 141, 142, 143, 144, 146, 147, 148, 149, 151, 153, 156, 159, 162, 165, 169, 170, 171, 172, 174, 175, 177, 178, 180, 183, 184, 185, 186, 187, 188, 189, 190, 193, 195, 200, 204, 206, 207, 208, 210, 211, 213, 216, 217, 220, 221, 224, 225, 232, 234, 239, 240, 242, 244, 246, 247, 248, 249, 250, 252, 253, 257, 259, 260, 263, 264, 266]

#makeArff(kospiCSV, f)
#deleteFeatures(csv_path, deletelist, f) ,f = open("../data/arff_ver2/afterFS/4/22/fs_2007_2010.arff",'w')
# arff_fs_22_2007_2010 = open("../data/arff_ver2/afterFS/4/22/fs_2007_2010.arff",'w')
# origin_2007_2010 = pd.read_csv('../data/2007-2010.csv')


#지수부터 해보자(index)
#학습
# deleteFeatures('./second(before_preprocessing)/index/4/22/2007_2008.csv', index_2007_2008, open('./third(after_preprocessing)/index/4/22/2007_2008.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/22/2009_2010.csv', index_2009_2010, open('./third(after_preprocessing)/index/4/22/2009_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/22/2011_2012.csv', index_2011_2012, open('./third(after_preprocessing)/index/4/22/2011_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/22/2013_2014.csv', index_2013_2014, open('./third(after_preprocessing)/index/4/22/2013_2014.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/22/2015_2016.csv', index_2015_2016, open('./third(after_preprocessing)/index/4/22/2015_2016.arff','w'))

# deleteFeatures('./second(before_preprocessing)/index/4/31/2007_2009.csv', index_2007_2009, open('./third(after_preprocessing)/index/4/31/2007_2009.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/31/2009_2011.csv', index_2009_2011, open('./third(after_preprocessing)/index/4/31/2009_2011.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/31/2011_2013.csv', index_2011_2013, open('./third(after_preprocessing)/index/4/31/2011_2013.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/31/2013_2015.csv', index_2013_2015, open('./third(after_preprocessing)/index/4/31/2013_2015.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/31/2015_2017.csv', index_2015_2017, open('./third(after_preprocessing)/index/4/31/2015_2017.arff','w'))

# deleteFeatures('./second(before_preprocessing)/index/6/33/2007_2009.csv', index_2007_2009, open('./third(after_preprocessing)/index/6/33/2007_2009.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/6/33/2010_2012.csv', index_2010_2012, open('./third(after_preprocessing)/index/6/33/2010_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/6/33/2013_2015.csv', index_2013_2015, open('./third(after_preprocessing)/index/6/33/2013_2015.arff','w'))

# deleteFeatures('./second(before_preprocessing)/index/6/42/2007_2010.csv', index_2007_2010, open('./third(after_preprocessing)/index/6/42/2007_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/6/42/2010_2013.csv', index_2010_2013, open('./third(after_preprocessing)/index/6/42/2010_2013.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/6/42/2013_2016.csv', index_2013_2016, open('./third(after_preprocessing)/index/6/42/2013_2016.arff','w'))

# deleteFeatures('./second(before_preprocessing)/index/8/44/2007_2010.csv', index_2007_2010, open('./third(after_preprocessing)/index/8/44/2007_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/8/44/2011_2014.csv', index_2011_2014, open('./third(after_preprocessing)/index/8/44/2011_2014.arff','w'))

# deleteFeatures('./second(before_preprocessing)/index/8/53/2007_2011.csv', index_2007_2011, open('./third(after_preprocessing)/index/8/53/2007_2011.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/8/53/2011_2015.csv', index_2011_2015, open('./third(after_preprocessing)/index/8/53/2011_2015.arff','w'))

# #테스트
# deleteFeatures('./second(before_preprocessing)/index/4/22_test/2009_2010.csv', index_2007_2008, open('./third(after_preprocessing)/index/4/22_test/2009_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/22_test/2011_2012.csv', index_2009_2010, open('./third(after_preprocessing)/index/4/22_test/2011_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/22_test/2013_2014.csv', index_2011_2012, open('./third(after_preprocessing)/index/4/22_test/2013_2014.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/22_test/2015_2016.csv', index_2013_2014, open('./third(after_preprocessing)/index/4/22_test/2015_2016.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/22_test/2017_2018.csv', index_2015_2016, open('./third(after_preprocessing)/index/4/22_test/2017_2018.arff','w'))

# deleteFeatures('./second(before_preprocessing)/index/4/31_test/2010_2010.csv', index_2007_2009, open('./third(after_preprocessing)/index/4/31_test/2010_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/31_test/2012_2012.csv', index_2009_2011, open('./third(after_preprocessing)/index/4/31_test/2012_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/31_test/2014_2014.csv', index_2011_2013, open('./third(after_preprocessing)/index/4/31_test/2014_2014.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/31_test/2016_2016.csv', index_2013_2015, open('./third(after_preprocessing)/index/4/31_test/2016_2016.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/4/31_test/2018_2018.csv', index_2015_2017, open('./third(after_preprocessing)/index/4/31_test/2018_2018.arff','w'))

# deleteFeatures('./second(before_preprocessing)/index/6/33_test/2010_2012.csv', index_2007_2009, open('./third(after_preprocessing)/index/6/33_test/2010_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/6/33_test/2013_2015.csv', index_2010_2012, open('./third(after_preprocessing)/index/6/33_test/2013_2015.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/6/33_test/2016_2018.csv', index_2013_2015, open('./third(after_preprocessing)/index/6/33_test/2016_2018.arff','w'))

# deleteFeatures('./second(before_preprocessing)/index/6/42_test/2011_2012.csv', index_2007_2010, open('./third(after_preprocessing)/index/6/42_test/2011_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/6/42_test/2014_2015.csv', index_2010_2013, open('./third(after_preprocessing)/index/6/42_test/2014_2015.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/6/42_test/2017_2018.csv', index_2013_2016, open('./third(after_preprocessing)/index/6/42_test/2017_2018.arff','w'))

# deleteFeatures('./second(before_preprocessing)/index/8/44_test/2011_2014.csv', index_2007_2010, open('./third(after_preprocessing)/index/8/44_test/2011_2014.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/8/44_test/2015_2018.csv', index_2011_2014, open('./third(after_preprocessing)/index/8/44_test/2015_2018.arff','w'))

# deleteFeatures('./second(before_preprocessing)/index/8/53_test/2012_2014.csv', index_2007_2011, open('./third(after_preprocessing)/index/8/53_test/2012_2014.arff','w'))
# deleteFeatures('./second(before_preprocessing)/index/8/53_test/2016_2018.csv', index_2011_2015, open('./third(after_preprocessing)/index/8/53_test/2016_2018.arff','w'))

# #변화량 해보자(delta)
# #학습
# deleteFeatures('./second(before_preprocessing)/delta/4/22/2007_2008.csv', delta_2007_2008, open('./third(after_preprocessing)/delta/4/22/2007_2008.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/22/2009_2010.csv', delta_2009_2010, open('./third(after_preprocessing)/delta/4/22/2009_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/22/2011_2012.csv', delta_2011_2012, open('./third(after_preprocessing)/delta/4/22/2011_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/22/2013_2014.csv', delta_2013_2014, open('./third(after_preprocessing)/delta/4/22/2013_2014.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/22/2015_2016.csv', delta_2015_2016, open('./third(after_preprocessing)/delta/4/22/2015_2016.arff','w'))

# deleteFeatures('./second(before_preprocessing)/delta/4/31/2007_2009.csv', delta_2007_2009, open('./third(after_preprocessing)/delta/4/31/2007_2009.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/31/2009_2011.csv', delta_2009_2011, open('./third(after_preprocessing)/delta/4/31/2009_2011.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/31/2011_2013.csv', delta_2011_2013, open('./third(after_preprocessing)/delta/4/31/2011_2013.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/31/2013_2015.csv', delta_2013_2015, open('./third(after_preprocessing)/delta/4/31/2013_2015.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/31/2015_2017.csv', delta_2015_2017, open('./third(after_preprocessing)/delta/4/31/2015_2017.arff','w'))

# deleteFeatures('./second(before_preprocessing)/delta/6/33/2007_2009.csv', delta_2007_2009, open('./third(after_preprocessing)/delta/6/33/2007_2009.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/6/33/2010_2012.csv', delta_2010_2012, open('./third(after_preprocessing)/delta/6/33/2010_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/6/33/2013_2015.csv', delta_2013_2015, open('./third(after_preprocessing)/delta/6/33/2013_2015.arff','w'))

# deleteFeatures('./second(before_preprocessing)/delta/6/42/2007_2010.csv', delta_2007_2010, open('./third(after_preprocessing)/delta/6/42/2007_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/6/42/2010_2013.csv', delta_2010_2013, open('./third(after_preprocessing)/delta/6/42/2010_2013.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/6/42/2013_2016.csv', delta_2013_2016, open('./third(after_preprocessing)/delta/6/42/2013_2016.arff','w'))

# deleteFeatures('./second(before_preprocessing)/delta/8/44/2007_2010.csv', delta_2007_2010, open('./third(after_preprocessing)/delta/8/44/2007_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/8/44/2011_2014.csv', delta_2011_2014, open('./third(after_preprocessing)/delta/8/44/2011_2014.arff','w'))

# deleteFeatures('./second(before_preprocessing)/delta/8/53/2007_2011.csv', delta_2007_2011, open('./third(after_preprocessing)/delta/8/53/2007_2011.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/8/53/2011_2015.csv', delta_2011_2015, open('./third(after_preprocessing)/delta/8/53/2011_2015.arff','w'))

# #테스트
# deleteFeatures('./second(before_preprocessing)/delta/4/22_test/2009_2010.csv', delta_2007_2008, open('./third(after_preprocessing)/delta/4/22_test/2009_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/22_test/2011_2012.csv', delta_2009_2010, open('./third(after_preprocessing)/delta/4/22_test/2011_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/22_test/2013_2014.csv', delta_2011_2012, open('./third(after_preprocessing)/delta/4/22_test/2013_2014.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/22_test/2015_2016.csv', delta_2013_2014, open('./third(after_preprocessing)/delta/4/22_test/2015_2016.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/22_test/2017_2018.csv', delta_2015_2016, open('./third(after_preprocessing)/delta/4/22_test/2017_2018.arff','w'))

# deleteFeatures('./second(before_preprocessing)/delta/4/31_test/2010_2010.csv', delta_2007_2009, open('./third(after_preprocessing)/delta/4/31_test/2010_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/31_test/2012_2012.csv', delta_2009_2011, open('./third(after_preprocessing)/delta/4/31_test/2012_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/31_test/2014_2014.csv', delta_2011_2013, open('./third(after_preprocessing)/delta/4/31_test/2014_2014.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/31_test/2016_2016.csv', delta_2013_2015, open('./third(after_preprocessing)/delta/4/31_test/2016_2016.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/4/31_test/2018_2018.csv', delta_2015_2017, open('./third(after_preprocessing)/delta/4/31_test/2018_2018.arff','w'))

# deleteFeatures('./second(before_preprocessing)/delta/6/33_test/2010_2012.csv', delta_2007_2009, open('./third(after_preprocessing)/delta/6/33_test/2010_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/6/33_test/2013_2015.csv', delta_2010_2012, open('./third(after_preprocessing)/delta/6/33_test/2013_2015.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/6/33_test/2016_2018.csv', delta_2013_2015, open('./third(after_preprocessing)/delta/6/33_test/2016_2018.arff','w'))

# deleteFeatures('./second(before_preprocessing)/delta/6/42_test/2011_2012.csv', delta_2007_2010, open('./third(after_preprocessing)/delta/6/42_test/2011_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/6/42_test/2014_2015.csv', delta_2010_2013, open('./third(after_preprocessing)/delta/6/42_test/2014_2015.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/6/42_test/2017_2018.csv', delta_2013_2016, open('./third(after_preprocessing)/delta/6/42_test/2017_2018.arff','w'))

# deleteFeatures('./second(before_preprocessing)/delta/8/44_test/2011_2014.csv', delta_2007_2010, open('./third(after_preprocessing)/delta/8/44_test/2011_2014.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/8/44_test/2015_2018.csv', delta_2011_2014, open('./third(after_preprocessing)/delta/8/44_test/2015_2018.arff','w'))

# deleteFeatures('./second(before_preprocessing)/delta/8/53_test/2012_2014.csv', delta_2007_2011, open('./third(after_preprocessing)/delta/8/53_test/2012_2014.arff','w'))
# deleteFeatures('./second(before_preprocessing)/delta/8/53_test/2016_2018.csv', delta_2011_2015, open('./third(after_preprocessing)/delta/8/53_test/2016_2018.arff','w'))


################################################################################################################
# #전체 무분할 데이터 특징선택 적용!
# deleteFeatures('./second(before_preprocessing)/whole/index/2007_2010.csv', index_2007_2008, open('./third(after_preprocessing)/whole/index/4/22/2007_2008.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/index/2009_2012.csv', index_2009_2010, open('./third(after_preprocessing)/whole/index/4/22/2009_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/index/2011_2014.csv', index_2011_2012, open('./third(after_preprocessing)/whole/index/4/22/2011_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/index/2013_2016.csv', index_2013_2014, open('./third(after_preprocessing)/whole/index/4/22/2013_2014.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/index/2015_2018.csv', index_2015_2016, open('./third(after_preprocessing)/whole/index/4/22/2015_2016.arff','w'))

# deleteFeatures('./second(before_preprocessing)/whole/index/2007_2010.csv', index_2007_2009, open('./third(after_preprocessing)/whole/index/4/31/2007_2009.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/index/2009_2012.csv', index_2009_2011, open('./third(after_preprocessing)/whole/index/4/31/2009_2011.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/index/2011_2014.csv', index_2011_2013, open('./third(after_preprocessing)/whole/index/4/31/2011_2013.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/index/2013_2016.csv', index_2013_2015, open('./third(after_preprocessing)/whole/index/4/31/2013_2015.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/index/2015_2018.csv', index_2015_2017, open('./third(after_preprocessing)/whole/index/4/31/2015_2017.arff','w'))

# deleteFeatures('./second(before_preprocessing)/whole/index/2007_2012.csv', index_2007_2009, open('./third(after_preprocessing)/whole/index/6/33/2007_2009.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/index/2010_2015.csv', index_2010_2012, open('./third(after_preprocessing)/whole/index/6/33/2010_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/index/2013_2018.csv', index_2013_2015, open('./third(after_preprocessing)/whole/index/6/33/2013_2015.arff','w'))

# deleteFeatures('./second(before_preprocessing)/whole/index/2007_2012.csv', index_2007_2010, open('./third(after_preprocessing)/whole/index/6/42/2007_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/index/2010_2015.csv', index_2010_2013, open('./third(after_preprocessing)/whole/index/6/42/2010_2013.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/index/2013_2018.csv', index_2013_2016, open('./third(after_preprocessing)/whole/index/6/42/2013_2016.arff','w'))

# deleteFeatures('./second(before_preprocessing)/whole/index/2007_2014.csv', index_2007_2010, open('./third(after_preprocessing)/whole/index/8/44/2007_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/index/2011_2018.csv', index_2011_2014, open('./third(after_preprocessing)/whole/index/8/44/2011_2014.arff','w'))

# deleteFeatures('./second(before_preprocessing)/whole/index/2007_2014.csv', index_2007_2011, open('./third(after_preprocessing)/whole/index/8/53/2007_2011.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/index/2011_2018.csv', index_2011_2015, open('./third(after_preprocessing)/whole/index/8/53/2011_2015.arff','w'))

# #변화량 해보자(delta)
# #학습
# deleteFeatures('./second(before_preprocessing)/whole/delta/2007_2010.csv', delta_2007_2008, open('./third(after_preprocessing)/whole/delta/4/22/2007_2008.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/delta/2009_2012.csv', delta_2009_2010, open('./third(after_preprocessing)/whole/delta/4/22/2009_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/delta/2011_2014.csv', delta_2011_2012, open('./third(after_preprocessing)/whole/delta/4/22/2011_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/delta/2013_2016.csv', delta_2013_2014, open('./third(after_preprocessing)/whole/delta/4/22/2013_2014.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/delta/2015_2018.csv', delta_2015_2016, open('./third(after_preprocessing)/whole/delta/4/22/2015_2016.arff','w'))

# deleteFeatures('./second(before_preprocessing)/whole/delta/2007_2010.csv', delta_2007_2009, open('./third(after_preprocessing)/whole/delta/4/31/2007_2009.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/delta/2009_2012.csv', delta_2009_2011, open('./third(after_preprocessing)/whole/delta/4/31/2009_2011.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/delta/2011_2014.csv', delta_2011_2013, open('./third(after_preprocessing)/whole/delta/4/31/2011_2013.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/delta/2013_2016.csv', delta_2013_2015, open('./third(after_preprocessing)/whole/delta/4/31/2013_2015.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/delta/2015_2018.csv', delta_2015_2017, open('./third(after_preprocessing)/whole/delta/4/31/2015_2017.arff','w'))

# deleteFeatures('./second(before_preprocessing)/whole/delta/2007_2012.csv', delta_2007_2009, open('./third(after_preprocessing)/whole/delta/6/33/2007_2009.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/delta/2010_2015.csv', delta_2010_2012, open('./third(after_preprocessing)/whole/delta/6/33/2010_2012.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/delta/2013_2018.csv', delta_2013_2015, open('./third(after_preprocessing)/whole/delta/6/33/2013_2015.arff','w'))

# deleteFeatures('./second(before_preprocessing)/whole/delta/2007_2012.csv', delta_2007_2010, open('./third(after_preprocessing)/whole/delta/6/42/2007_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/delta/2010_2015.csv', delta_2010_2013, open('./third(after_preprocessing)/whole/delta/6/42/2010_2013.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/delta/2013_2018.csv', delta_2013_2016, open('./third(after_preprocessing)/whole/delta/6/42/2013_2016.arff','w'))

# deleteFeatures('./second(before_preprocessing)/whole/delta/2007_2014.csv', delta_2007_2010, open('./third(after_preprocessing)/whole/delta/8/44/2007_2010.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/delta/2011_2018.csv', delta_2011_2014, open('./third(after_preprocessing)/whole/delta/8/44/2011_2014.arff','w'))

# deleteFeatures('./second(before_preprocessing)/whole/delta/2007_2014.csv', delta_2007_2011, open('./third(after_preprocessing)/whole/delta/8/53/2007_2011.arff','w'))
# deleteFeatures('./second(before_preprocessing)/whole/delta/2011_2018.csv', delta_2011_2015, open('./third(after_preprocessing)/whole/delta/8/53/2011_2015.arff', 'w'))

deleteFeatures('./second(before_preprocessing)/whole/rate/2013_2016.csv', rate_2013_2014, open('./third(after_preprocessing)/whole/rate/4/22/2015_2016.arff', 'w'))

#######################################################################################################################################
#특징선택없는 전체 데이터!
# 지수(index)
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/index/2007_2010.csv'), open('./third(after_preprocessing)/whole_normal/index/2007_2010.arff', 'w'))
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/index/2009_2012.csv'), open('./third(after_preprocessing)/whole_normal/index/2009_2012.arff', 'w'))
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/index/2011_2014.csv'), open('./third(after_preprocessing)/whole_normal/index/2011_2014.arff', 'w'))
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/index/2013_2016.csv'), open('./third(after_preprocessing)/whole_normal/index/2013_2016.arff', 'w'))
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/index/2015_2018.csv'), open('./third(after_preprocessing)/whole_normal/index/2015_2018.arff', 'w'))

# makeArff(pd.read_csv('./second(before_preprocessing)/whole/index/2007_2012.csv'), open('./third(after_preprocessing)/whole_normal/index/2007_2012.arff', 'w'))
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/index/2010_2015.csv'), open('./third(after_preprocessing)/whole_normal/index/2010_2015.arff', 'w'))
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/index/2013_2018.csv'), open('./third(after_preprocessing)/whole_normal/index/2013_2018.arff', 'w'))

# makeArff(pd.read_csv('./second(before_preprocessing)/whole/index/2007_2014.csv'), open('./third(after_preprocessing)/whole_normal/index/2007_2014.arff', 'w'))
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/index/2011_2018.csv'), open('./third(after_preprocessing)/whole_normal/index/2011_2018.arff', 'w'))

# # #변화량 해보자(delta)
# # #학습
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/delta/2007_2010.csv'), open('./third(after_preprocessing)/whole_normal/delta/2007_2010.arff', 'w'))
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/delta/2009_2012.csv'), open('./third(after_preprocessing)/whole_normal/delta/2009_2012.arff', 'w'))
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/delta/2011_2014.csv'), open('./third(after_preprocessing)/whole_normal/delta/2011_2014.arff', 'w'))
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/delta/2013_2016.csv'), open('./third(after_preprocessing)/whole_normal/delta/2013_2016.arff', 'w'))
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/delta/2015_2018.csv'), open('./third(after_preprocessing)/whole_normal/delta/2015_2018.arff', 'w'))

# makeArff(pd.read_csv('./second(before_preprocessing)/whole/delta/2007_2012.csv'), open('./third(after_preprocessing)/whole_normal/delta/2007_2012.arff', 'w'))
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/delta/2010_2015.csv'), open('./third(after_preprocessing)/whole_normal/delta/2010_2015.arff', 'w'))
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/delta/2013_2018.csv'), open('./third(after_preprocessing)/whole_normal/delta/2013_2018.arff', 'w'))

# makeArff(pd.read_csv('./second(before_preprocessing)/whole/delta/2007_2014.csv'), open('./third(after_preprocessing)/whole_normal/delta/2007_2014.arff', 'w'))
# makeArff(pd.read_csv('./second(before_preprocessing)/whole/delta/2011_2018.csv'), open('./third(after_preprocessing)/whole_normal/delta/2011_2018.arff', 'w'))
