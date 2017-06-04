from pygame import *

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR =  "#888888"
JUMP_POWER = 10
GRAVITY = 0.35 # ����, ������� ����� ������ ��� ����

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0   #�������� �����������. 0 - ������ �� �����
        self.startX = x # ��������� ������� �, ���������� ����� ����� ������������ �������
        self.startY = y
        self.yvel = 0 # �������� ������������� �����������
        self.onGround = False # �� ����� �� �?
        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT) # ������������� ������
        self.image.set_colorkey(Color(COLOR)) # ������ ��� ����������

    def update(self, left, right, up, platforms):
        
        if up:
            if self.onGround: # �������, ������ ����� ����� ������������ �� �����
                self.yvel = -JUMP_POWER
            self.image.fill(Color(COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))
               
                       
        if left:
            self.xvel = -MOVE_SPEED # ���� = x- n
            self.image.fill(Color(COLOR))
            if up: # ��� ������ ����� ���� ��������� ��������
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))
 
        if right:
            self.xvel = MOVE_SPEED # ����� = x + n
            self.image.fill(Color(COLOR))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))
         
        if not(left or right): # �����, ����� ��� �������� ����
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))
            
        if not self.onGround:
            self.yvel +=  GRAVITY
            
        self.onGround = False; # �� �� �����, ����� �� �� �����((   
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel # ��������� ���� ��������� �� xvel
        self.collide(self.xvel, 0, platforms)
   
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p): # ���� ���� ����������� ��������� � �������

                if xvel > 0:                      # ���� �������� ������
                    self.rect.right = p.rect.left # �� �� �������� ������

                if xvel < 0:                      # ���� �������� �����
                    self.rect.left = p.rect.right # �� �� �������� �����

                if yvel > 0:                      # ���� ������ ����
                    self.rect.bottom = p.rect.top # �� �� ������ ����
                    self.onGround = True          # � ���������� �� ���-�� �������
                    self.yvel = 0                 # � ������� ������� ���������

                if yvel < 0:                      # ���� �������� �����
                    self.rect.top = p.rect.bottom # �� �� �������� �����
                    self.yvel = 0                 # � ������� ������ ���������
       
