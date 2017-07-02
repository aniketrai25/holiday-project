import pygame
import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats

def run_game():
    # Start the game and create a screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Holiday Project")

    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create an instance to store game statistics
    stats = GameStats(ai_settings)
    
    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)




run_game()
