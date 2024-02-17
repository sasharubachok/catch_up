from pygame import* 

window =display.set_mode((700,500))  
class GameSprite(): 
    def __init__(self, img, x, y , speed): 
        self.img = transform.scale(image.load(img), (65,65)) 
        self.rect = self.img.get_rect() 
        self.rect.x = x 
        self.rect.y = y 
        self.speed = speed
        self.move_left = False 

       
         
    def reset(self):
        if self.move_left == True: 
           self.rect.x += self.speed 
        window.blit(self.img, (self.rect.x, self.rect.y))  

window = display.set_mode((700,500)) 

mixer.init() 
mixer.music.load('jungles.ogg') 
mixer.music.play() 

background = image.load('background.jpg')


game = True 
clock = time.Clock()

hero = GameSprite("hero.png", 50,50 , 10)
while game: 
    window.blit(background, (0,0)) 
    hero.reset()
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
        if e.type == KEYDOWN: 
            if e.key == K_1: 
                kick.play() 
            if e.key == K_d:  
                hero.move_left = True 

        if e.type == KEYUP: 
            if e.key == K_d: 
                hero.move_left = False 



    display.update() 
    clock.tick(60)

