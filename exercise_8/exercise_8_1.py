#import reportlap
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# create pdf function
def createPDF(outputPath, attributeDict, picturePath):
        # create canvas
        c = canvas.Canvas(outputPath,pagesize = letter)
        
        # set font
        c.setFont("Helvetica", 20)
        
        #write title
        c.drawString(150,760,f"Information for the district '{attributeDict['district_name']}'")
        
        #set font
        c.setFont("Helvetica", 14)
        
        #write information
        c.drawString(100,735,f"The parent district is : {attributeDict['parent']}.")
        c.drawString(100,705,f"The district has an area of {attributeDict['area']} m^2.")
        c.drawString(100,690,f"The district has  {attributeDict['house_number_count']} housenumbers.")
        c.drawString(100,675,f"The district contains {attributeDict['parcels_count']} parcels.")
        
        #if schools or pools are selected
        if (attributeDict['counted_property']!="None"):
            c.drawString(100,650,f"The counted property is '{attributeDict['counted_property']}'. There are {attributeDict['pool_or_school_count']} objects of this property.")
        
        #when not selected
        else:
            c.drawString(100,650,f"Please select pools or schools as point input.")
        
        # draw image of map when picturePath is given
        if picturePath:
            c.drawString(100,600,"Map of selected disrict:")
            c.drawImage(picturePath,100, 270, width = 400 , height = 300)
        
        #save canvas
        c.save()