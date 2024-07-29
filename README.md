# Comparison-of-LSB-and-CNN-for-Image-Steganography
Steganography can be defined as ”masking the existence of secret information.” There are many algorithms available to perform Steganography. In this project, we will be using the Least Significant Bit(abbreviated as LSB) technique to perform Steganography. In addition, we will be designing a Convolutional Neural Network to perform the same Steganography and perform a comparative study of the results obtained from the LSB technique and the CNN.

# Software Requirements
- Python 3
- Google Colab (Online tool)
- Jupyter notebook (If Google Colab isn't available)

# Libraries
- Tensorflow
- OpenCV
- Numpy
- GoogleDrive Library

# How to Run :
1) 1 Bit LSB and 4 Bit LSB code can be run in command prompt.
2) For CNN Deep Steganography, upload the code onto Colab and upload the dataset to your google drive.
3) Load the dataset from the drive and follow instructions given below at - How to run CNN.
4) Train the model and run the code.
5) For PSNR and MSE, follow instructions given below at - How to run PSNR and MSE.

# Run 1 Bit LSB:
- Run the python code in  command prompt and make sure the secret and cover images are in 'images' folder and are in jpg format.
- Encryption : `steganography_1bit.py merge --img1=images/cover.jpg --img2=images/secret.jpg --output=images/cipher.png`.
- Decryption : `steganography_1bit.py unmerge --img=images/cipher.png --output=images/extracted.png`.

# Run 4 Bit LSB:
- Run the python code in  command prompt and make sure the secret and cover images are in 'images' folder and are in jpg format.
- Encryption : `steganography_4bit.py merge --img1=images/cover.jpg --img2=images/secret.jpg --output=images/cipher.png`.
- Decryption : `steganography_4bit.py unmerge --img=images/cipher.png --output=images/extracted.png`.

# Run CNN for Deep Steganography:
- First, change the train path (in the code, it is named as TRAIN_PATH) to the pathway in which you have stored the dataset. It is better if you store the dataset in your google drive. For example, the pathway I have given in my system is : `/content/drive/My Drive/Semantic dataset100/`. Here, “Semantic dataset100” is the name of the dataset.

- Next, change the LOGS_Path and the CHECKPOINTS_PATH pathways to something of your liking. Again, it is preferred if these directories are stored in google drive. Create two separate folders in your drive for this purpose. For example, in my system, LOGS_Path = `/content/drive/My Drive/StegLogs/` and CHECKPOINTS_PATH = `/content/drive/My Drive/StegOutput/`.

- After this, run all the cells sequentially in order upto cell number 12. This cell is the cell where the training of the neural network takes place. It may run for more than a few days. Let it. Do not execute any other part of the code in this time.

- Now after 12 hours, the connection to the GPU on google colab times out. At this point, go back to cell number 10. You will see a line that says `saver.save()` and some arguments within paranthesis. The line is initially commented out(denoted by #). Uncomment that line, maintain exactly the same syntax and only alter the value for the global_step variable, depending on the last saved checkpoint file.

- Go to the checkpoint directory in your drive. Each file in it is named based on its global step value. There are 3 types of files for each global step. They are “.data file”, “.index file” and “.meta file”. We are only concerned with the “.meta file”. Take the “.meta” file with the largest number and enter that number for the global_step variable. Then execute from cell number 1 again upto cell 12.

- Keep repeating this until you feel that the neural network has been trained enough.

- Once this is done, run cell number 13 as it is.

- From cell number 14 to the end, type the following code at the beginning of each cell :-    
```ruby
with tf.Session() as sess:
    saver = tf.train.import_meta_graph('/content/drive/My Drive/StegOutput/beta_0.75.chkp-30865.meta/')
    saver.restore(sess, '/content/drive/My Drive/StegOutput/beta_0.75.chkp-30865')
```

- Change the value 30865 to whatever global_step value you had given last in cell number 10. 30865 is what I obtained in my training. It may be different for different systems. Also, if needed, change the directory name from “StegOutput” to whatever directory name you have given for the directory where your checkpoint files are stored.If you wish to save the inputs and outputted data for further operations, then create two folders and type out the following code at the end of cell number 14:- 
```ruby
`plt.imsave('/content/drive/My Drive/StegInput/cover.png', denormalize_batch(cover))
plt.imsave('/content/drive/My Drive/StegInput/secret.png', denormalize_batch(secret))
```

- Here, “StegInput” is the name I have given for the directory which stores the input files. You can change the name to whatever you would like.
For the Stego Image, use the following code at the end of cell number 15:-
`plt.imsave('/content/drive/My Drive/StegSave/output.png', denormalize_batch(hidden.squeeze()))`
Again, Stegsave is simply a directory name and can be altered according to your preferrence. This directory stores the outputted Stego Image.

- Use this code at the end of cell 16 for the revealed secret image.
`plt.imsave('/content/drive/My Drive/StegSave/output1.png', denormalize_batch(revealed.squeeze()))`
Now you can run the cells sequentially in order from cell 14 upto the end.
        
# Run PSNR:
- Run the python code in  command prompt and make sure the secret and extracted images are in 'images' folder.