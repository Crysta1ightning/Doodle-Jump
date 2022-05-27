# Doodle-Jump
A neat based AI learning doodle jump game

Below is a preview of the game:

![image](https://user-images.githubusercontent.com/49239376/170732169-1ee19aad-3300-4466-9d54-ef965d553b03.png)

The objective is to train a doodle that can jump infinetly high (get infinite score)
We train 100 doodle per round and some doodle is supposed to understand that it needs to land on the platforms inorder to gain more scores.
We give rewards to the doodle when it jumps on a platform, and when it jumps higher, this way it could learn how to win by itself.

After many trials, we will train one successful doodle.
When this doodle locates the closest platform, it'll move diagonally to that platform.
Then, this doodle will goes left and right repeadetly (so that it could stay on the x position).
As soon as this doodle learns that, it will be able to jump infinetly high.

![image](https://user-images.githubusercontent.com/49239376/170735487-7591fd5e-2ced-40fa-b4f9-a60b2451fefc.png)
