from  mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getPos()

mc.setBlocks(x-1,y-1,z-1,x-10,y-10,z-10,46,1)

while True:
    x,y,z=mc.player.getPos()
    mc.setBlock(x,y-2,z,46,1)


