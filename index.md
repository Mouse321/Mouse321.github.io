Space Invaders
=============

Description
----------
 Oh no! The aliens are attacking, HELP!                                                                                                                                   
 In order to save our beloved planet, you must play this game to fight off the aliens!                                                                                   
 YOUR job is to shoot down the aliens with a tank!                                                                                                                      

Features
-------
- multile difficulties
- different types of weapons
- movable tanks

Interesting Code
----------------
This is how the seeking bullet works
```python
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
```

Game Preview (Easy Mode)
------------
![image](https://user-images.githubusercontent.com/80147845/230703370-decdd83d-264a-46d8-876c-eac4e952974a.png)

Game Preview (Hard Mode)
------------
![image](https://user-images.githubusercontent.com/80147845/230703449-0895a327-9c64-4e0c-b22d-afdab275cea9.png)



Method
------
  1. First, I made the points where the aliens will travel to!
  2. Next, I made aliens, tanks and bullets!
  3. Finally, I made a new difficulty, Hard Mode!
  
Resources
---------
- pycat/python
- [Tank and bullets](https://www.pixilart.com/art/tanks-0b452a9c87d9f9b), by Duderisfound
