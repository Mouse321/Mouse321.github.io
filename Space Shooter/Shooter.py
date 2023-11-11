from pycat.core import Window, Sprite, Color, Point, RotationMode, KeyCode, Scheduler
import random
window = Window(background_image= 'Background.jpg')
window.background_sprite.scale = 1.5
Hardmode = False
waypoints = [
    Point(1000, 500),
    Point(50, 500),
    Point(50, 400),
    Point(1200, 400),
    Point(1200, 300),
    Point(50, 300),
    Point(50, 200),
    Point(10000, 200),
]

class Alien(Sprite):
    def on_create(self):
        self.image = 'Enemy.png'
        self.index = 0
        self.scale = 0.25
        self.add_tag('Alien')
        self.position = 1200, 500
        self.rotation_mode = RotationMode.RIGHT_LEFT
        if Hardmode == True:
            self.color = Color.GREEN
            self.scale = 0.2
    def on_update(self, dt):
        target = waypoints[self.index]
        self.point_toward(target)
        self.move_forward(5)
        if self.distance_to(target) < 10:
            self.index += 1
        if self.is_touching_window_edge():
            self.delete()
        if Hardmode == True:
            self.move_forward(7.5)

class Hardmodebutton(Sprite):
    def on_create(self):
        self.image = 'HardMode.png'
        self.position = 300,100
        self.scale = 0.5
    def on_left_click(self):
        for sprite in window.get_sprites_with_tag('Alien'):
            sprite.color = Color.GREEN
        global Hardmode
        Hardmode = True
    def on_update(self, dt):
        if Hardmode == True:
            self.color = Color.random_rgb()

class Tank(Sprite):
    def on_create(self):
        self.cooldown1 = 1
        self.cooldown2 = 2
        self.image = 'Tank.png'
        self.rotation = 90
        self.position = 600,100
        self.scale = 0.25
    def on_update(self, dt):
        self.cooldown1 -= dt
        self.cooldown2 -= dt
        if window.is_key_down(KeyCode.SPACE) and self.cooldown1 <= 0.1:
            window.create_sprite(Bullet, position = self.position)
            self.cooldown1 = 1
        if window.is_key_down(KeyCode.G) and self.cooldown2 <= 0.1:
            window.create_sprite(Sbullets, position = self.position)
            window.create_sprite(Sbullets, position = self.position)
            self.cooldown2 = 2
        if window.is_key_pressed(KeyCode.RIGHT):
            self.x += 5
        if window.is_key_pressed(KeyCode.LEFT):
            self.x -= 5
class Bullet(Sprite):
    def on_create(self):
        self.image = 'Bullet.png'
        self.add_tag('Bullet')
        self.scale = 0.4
        self.rotation = 90
        if Hardmode == True:
            self.scale = 0.3
    def on_update(self, dt):
        for sprite in self.get_touching_sprites_with_tag('Alien'):
            self.delete()
            sprite.delete()
            
        self.move_forward(50)
        if self.is_touching_window_edge():
            self.delete()
class Sbullets(Sprite):
    def on_create(self):
        self.timer = 0
        self.scale = 0.25
        self.image = 'Sbullets.png'
        self.add_tag('Sbullets')
        self.rotation = random.randint(0,360)
        self.target = random.choice(window.get_sprites_with_tag('Alien'))
        if Hardmode == True:
            self.timer = 1
    def on_update(self, dt):
        self.timer += dt
        if self.timer >= 1.8:
            self.delete()
        self.point_toward_sprite(self.target)
        self.move_forward(7)
        for sprite in self.get_touching_sprites_with_tag('Alien'):
            sprite.delete()
            self.delete()
        if self.is_touching_window_edge():
            self.delete()



Scheduler.update(lambda: window.create_sprite(Alien), 0.5)
window.create_sprite(Hardmodebutton)
window.create_sprite(Tank)
window.create_sprite(Alien)
window.run()    