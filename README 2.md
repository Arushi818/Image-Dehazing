# course-project-comp3301-project-arushi
course-project-comp3301-project-arushi created by GitHub Classroom

## About the code:
### Acknowledgement: 

__This is to acknowledge that the code mentioned in this repository was found on the following repository:__
    [https://github.com/arjundixit98/Defogging-Images-using-Dark-Channel-Prior]

  __Note:__
  
   -The code from that repository was very slightly tweaked to be able to experiment with soft matting and compare against the guided filter used in the code.
     The library below was used for soft matting:
     [https://github.com/MarcoForte/closed-form-matting] (although the use of this library is still a work in progress)

   -The code is simply being tested and studied in this project.

### Background information:

- The source code is based on the dark channel prior, originally proposed in the paper entitled "Single image haze removal using dark channel prior", published in 2010 by Kaiming He, Jian Sun and Xiaoou Tang.(This paper can be found in the "papers" folder in this repository and has also been cited in this readme)
- The dark channel prior is based on the statistical observation that the patches (neighbourhood of pixels) of the local area (term coined in the paper, meaning the image excluding any sky area) of most outdoor haze-free images have at least one colour channel with a very low intensity (tending towards zero).
- This information is then used to dehaze images, based on calculations and estimations revolving around the aformentionned theory.(More on this in the upcoming report)

### Additional information about the code:

- Despite being based on the theory proposed in the paper, the code differs from the proposed method in that it tries to optimise the proposed method to allow for a quicker processing. For instance, it uses a guided filter instead of the soft-matting in the paper to collect edge information.

### How To Run:
__Steps:__
1. Open a terminal or command prompt
2. Change the directory to the folder where the haze_removal.py and gf.py scripts are located
3. To run the script, enter the command as follows:
   
       python3 haze_removal.py <"complete path to image to be dehazed">
  
#### Note:
  1. Ignore the deprecation warnings upon running the code
  2. The resulting dehazed image, labelled "test.jpg", will be created and saved in the same folder as the "haze_removal.py" script after       running the code. The image has to be renamed and moved to the appropriate folder.



## Contents of the Repository:

- "Papers folder" contains all the papers being used or to be used  
- "Source Code" contains 2 folders entitled:
   1. "Original_intent" which contains the unfinished script coded in an attempt to replicate the paper from the original project
   2. "Defogging-Images-using-Dark-Channel-Prior-master" which contains all the source code from the repository in the acknowledgement section (This includes code from the repository being studied and the 
       library being used for comparative purposes)
- "TestImagesandResults" contains several folders for several experimentations carried out to explore the code. This folder also includes test images along with their results, as well as explanatory images from 
   the repository in the acknowledgement section

## Explanation for change in project:

__The initial intent was to evaluate fog thickness while replicating the paper on this link:__ 
    https://www.mdpi.com/2073-4433/14/7/1125

- However, when asked for the source code, the publishers never responded with the code.

- An attempt was made to replicate the method proposed in the paper to evaluate fog thickness. The unfinished script, titled "fog_detect.py" can be found in the "Original_Intent" folder.

- After consulting the lecturer, I was advised to use pre-existing code and libraries due to time constraints and change the focus of the project to "Image Dehazing" since I am working on my own and had 
  an unexpected set-back

## References:
    Arun Dixit, “Defogging-Images-using-Dark-Channel-Prior” [Source Code], 2019,https://github.com/arjundixit98/Defogging-Images-using-Dark-Channel-Prior

    Kaiming He, Jian Sun and Xiaoou Tang, "Single image haze removal using dark channel prior," 2009 IEEE Conference on Computer Vision and Pattern Recognition, Miami, FL, 2009, pp. 1956-1963, doi: 
    10.1109/CVPR.2009.5206515.

    Lin, Zheqi, and Xuansheng Wang, “Dehazing for Image and Video Using Guided Filter,” Open Journal of Applied Sciences, vol. 02, no. 04, Jan. 2013, p. 123. www.scirp.org, 
    https://doi.org/10.4236/ojapps.2012.24B030.
    
    Jiahao Pang, Oscar C. Au and Zheng Guo, "Improved Single Image Dehazing Using Guided Filter,"The Hong Kong University of Science and Technology, Hong Kong,www.apsipa.org, 
    http://www.apsipa.org/proceedings_2011/pdf/apsipa198.pdf 
    

