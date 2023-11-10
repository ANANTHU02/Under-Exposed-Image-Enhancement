# Under-Exposed-Image-Enhancement

The primary goal of low-light image enhancement is to improve the image’s overall and local contrast, visual effect, and transformation into a form
more appropriate for human observation or computer processing while avoiding noise amplification and attaining high real-time performance. To that
aim, improving the validity and availability of data recorded in low-light conditions is critical to producing clear photographs or videos. Such enhancement can make images more consistent with individuals’ subjective visual perception and improve the reliability and robustness of outdoor optical systems. It can also make such images more easily analysed and processed by computer vision equipment, which is critical for promoting the development of image information mining.

Image Enhancement Techniques
-----------------------------

1. Linear Transformation - is a linear function of the gray values of the input image. A linear transformation of the gray values is also known
as linear stretching. The formula is as follows:
                                                g(x, y) = C · f(x, y) + R
Where f (x, y) and g(x, y) represent the input and output images, respectively, and C and R are the coefficients of the linear transformation.
Changing the coefficient values in the formula above can improve an image to various degrees. A common formula for a linear gray stretch
is as follows:
                                                g(x, y) = f(x, y) − fmin
                                                         ---------------- (gmax − gmin) + gmin
                                                          fmax − fmin
Where fmax and fmin represent the input image’s maximum and minimum gray values, respectively, and gmax and gmin represent the maximum and minimum gray values of the output image, respectively.Thus, the image’s dynamic range is transformed from [fmin, fmax] to [gmin, gmax] to enhance the brightness and contrast.


                                                         
