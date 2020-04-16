import pytesseract as tess
import  cv2
from PIL import Image
from selenium import webdriver

def img_to_text(captchaImage):
    tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    capImage = cv2.imread( captchaImage )
    capImageGray = cv2.cvtColor( capImage, cv2.COLOR_BGR2GRAY )
    (thresh, blackAndWhiteImage) = cv2.threshold( capImageGray, 127, 255, cv2.THRESH_BINARY )
    cv2.imshow( 'Black white image', blackAndWhiteImage )
    text = tess.image_to_string( capImageGray )
    print( "Captcha Image: " )
    print( text )
    cv2.imshow( "gray", capImageGray )
    if cv2.waitKey( 0 ) & 0xFF == 27:  # ord( 'q' ):
        cv2.destroyAllWindows()
        text = tess.image_to_string( blackAndWhiteImage )


def get_captcha_text(location, size):
    im = Image.open('screenshot.png')
    left = location['x'] +220
    top = location['y'] +40
    right = left + size['width']
    bottom = top + size['height']
    print(right)
    im = im.crop( (left, top, right, bottom) )  # defines crop points
    im.save('screenshot2.png')
    img_to_text('screenshot2.png')

def login_to_website(url):
  driver = webdriver.Chrome(executable_path="C://Users//zigron//Downloads//chromedriver_win32//chromedriver.exe")
  driver.get(url)
  driver.set_window_size(1120, 550)
  capElement  = driver.find_element_by_xpath('/html/body/div[1]/div/section/div/form/div/div[1]/input')
  location = capElement.location
  size = capElement.size
  get_captcha_text( location, size )
  driver.save_screenshot( 'screenshot.png' )
  img = cv2.imread('screenshot.png')
  img = cv2.circle(img,(location['x']+220, location['y']+40),5, (255,0,0), 3, cv2.LINE_AA)
  cv2.imwrite("circle.png",img)

login_to_website("https://www.dentalens.com/detection-demo")
exit()

