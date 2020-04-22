# Enter number of Blocks available
#
# Determine how many layers of pyramid can be made
#

blocks=int(input("Enter Number of Blocks in Hands: "))

blk_counter=0
layer_counter=0

while blocks>=(blk_counter+1):
	blk_counter+=1
	blocks=blocks-blk_counter
	layer_counter+=1

print("Number of Layers is:", layer_counter)

