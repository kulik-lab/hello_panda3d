from direct.showbase.ShowBase import ShowBase
#import direct.directbase.DirectStart
from panda3d.core import Material
import simplepbr




class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        simplepbr.init()

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        #render.setAntialias(AntialiasAttrib.MAuto)


        myMaterial = Material()
        myMaterial.setShininess(55.0) #Make this material shiny
        myMaterial.setAmbient((0, 1, 0, 1)) #Make this material blue

        myNode = loader.loadModel("zielcube2.gltf") #Load the model to apply the material to
        #myNode.clearTexture()
        #myNode.setMaterial(myMaterial) #Apply the material to this nodePath
        myNode.setPos(0,4,0)
        #myNode.setAntialias(AntialiasAttrib.MAuto)
        myNode.reparentTo(self.render)


app = MyApp()
app.run()
