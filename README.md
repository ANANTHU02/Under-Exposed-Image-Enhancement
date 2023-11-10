# Under-Exposed-Image-Enhancement

The primary goal of low-light image enhancement is to improve the image’s overall and local contrast, visual effect, and transformation into a form
more appropriate for human observation or computer processing while avoidinging noise amplification and attaining high real-time performance. To that
aim, improving the validity and availability of data recorded in low-light conditions is critical to producing clear photographs or videos. Such enhancement can make images more consistent with individuals’ subjective visual perception and improve the reliability and robustness of outdoor optical systems. It can also make such images more easily analyzed and processed by computer vision equipment, which is critical for promoting the development of image information mining.

Image Enhancement Techniques
-----------------------------

1. Linear Transformation - is a linear function of the gray values of the input image. A linear transformation of the gray values is also known
as linear stretching. The formula is as follows:
                                                g(x, y) = C · f(x, y) + R
Where f (x, y) and g(x, y) represent the input and output images, respectively, and C and R are the coefficients of the linear transformation.
Changing the coefficient values in the formula above can improve an image to various degrees. A common formula for a linear gray stretch
is as follows:
                                                g(x, y) = f(x, y) − fmin
                                                         ---------------- (gmax − gmin) + gmin
                                                          fmax − fmin
Where fmax and fmin represent the input image’s maximum and minimum gray values, respectively, and gmax and gmin represent the maximum and minimum gray values of the output image, respectively.Thus, the image’s dynamic range is transformed from [fmin, fmax] to [gmin, gmax] to enhance the brightness and contrast.

2.Histogram Equalization - An image exhibits great contrast and a wide dynamic range if the pixel values are uniformly distributed across all possible grey levels. Based on this characteristic, the HE algorithm uses the cumulative distribution function (CDF) to adjust the output gray levels to have a probability density function that corresponds to a uniform distribution; in this way, hidden details in dark areas can be made to reappear, and the visual effect of the input image can be effectively enhanced. Let I and L denote an image and its gray levels, respectively. I(i, j) represents the gray value at the position with coordinates (i,j), N represents the total number of pixels in the image, and nk represents the number of pixels of gray level k. Then, the gray-level probability
density function of the image I is defined as:

                                                  p(k) = nk / N     , (k = 0, 1, 2, ..., L − 1)

3.CLAHE(Contrast Limited Adaptive Histogram Equalization) - is a type of adaptive histogram equalization that addresses the issue of contrast over-amplification. Instead of processing the entire image, CLAHE works with discrete sections called tiles. The false borders are eliminated by combining the adjacent tiles using bi-linear interpolation. The results of equating only the luminance channel of an HSV image are far superior to those obtained by equating all the channels of the RGB image. CLAHE can also be applied to color images, where it is often applied on the luminance channel.
                                                    
                                                         

                                                         
