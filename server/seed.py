from app import create_app, db
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from datetime import date

def seed_database():
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Create sample users
        user1 = User(username='admin', password='password123')
        user2 = User(username='producer', password='producer123')
        
        db.session.add(user1)
        db.session.add(user2)
        
        # Create sample guests
        guests = [
            Guest(name='Jennifer Lawrence', occupation='Actress'),
            Guest(name='Stephen King', occupation='Author'),
            Guest(name='Elon Musk', occupation='Entrepreneur'),
            Guest(name='Taylor Swift', occupation='Singer'),
            Guest(name='Bill Gates', occupation='Philanthropist')
        ]
        
        for guest in guests:
            db.session.add(guest)
        
        # Create sample episodes
        episodes = [
            Episode(date=date(2024, 1, 15), number=1001),
            Episode(date=date(2024, 1, 16), number=1002),
            Episode(date=date(2024, 1, 17), number=1003),
            Episode(date=date(2024, 1, 18), number=1004),
            Episode(date=date(2024, 1, 19), number=1005)
        ]
        
        for episode in episodes:
            db.session.add(episode)
        
        # Commit to get IDs
        db.session.commit()
        
        # Create sample appearances
        appearances = [
            Appearance(rating=5, guest_id=1, episode_id=1),
            Appearance(rating=4, guest_id=2, episode_id=1),
            Appearance(rating=5, guest_id=3, episode_id=2),
            Appearance(rating=3, guest_id=4, episode_id=3),
            Appearance(rating=4, guest_id=5, episode_id=4),
            Appearance(rating=5, guest_id=1, episode_id=5)
        ]
        
        for appearance in appearances:
            db.session.add(appearance)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()