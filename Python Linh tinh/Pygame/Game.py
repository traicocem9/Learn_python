import pygame
import random
import sys
from os import path
pygame.init()

#img dir
img_dir = path.join(path.dirname(__file__), 'asset')


WIDTH = 800
HEIGHT = 600

RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BACKGROUND_COLOR = (0,0,0)

player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]

SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

score = 0

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)

def main_menu():
	global screen
	#menu_songg
	#pygame.mixer

	title = pygame.image.load(path.join(img_dir, "Mainmenu.png")).convert()
	title = pygame.transform.scale(title, (WIDTH, HEIGHT), screen)

	screen.blit(title,(0,0))
	pygame.display.update()

	while True:
        ev = pygame.event.poll()
		
		if ev.type == pygame.KEYDOWN:
			if ev.key == pygame.K_RETURN:
				break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        elif ev.type == pygame.QUIT:
                pygame.quit()
                quit() 
def set_level(score, SPEED):
	if score < 20:
		SPEED = 5
	elif score < 40:
		SPEED = 8
	elif score < 60:
		SPEED = 12
	else:
		SPEED = 15
	return SPEED
	# SPEED = score/5 + 1


def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.1:
		x_pos = random.randint(0,WIDTH-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] += SPEED
		else:
			enemy_list.pop(idx)
			score += 1
	return score

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False

def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
			return True
	return False

while not game_over:

	main_menu()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	keys = pygame.key.get_pressed()

	x = player_pos[0]
	y = player_pos[1]
	if keys[pygame.K_LEFT]:
		x -= 10
	if keys[pygame.K_RIGHT]:
		x += 10	
	player_pos = [x,y]

	screen.fill(BACKGROUND_COLOR)

	drop_enemies(enemy_list)
	score = update_enemy_positions(enemy_list, score)
	SPEED = set_level(score, SPEED)

	text = "Score:" + str(score)
	label = myFont.render(text, 1, YELLOW)
	screen.blit(label, (WIDTH-200, HEIGHT-40))

	if collision_check(enemy_list, player_pos):
		game_over = True
		break

	draw_enemies(enemy_list)

	pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

	clock.tick(30)

	pygame.display.update()
