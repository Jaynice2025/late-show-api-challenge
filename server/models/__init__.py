# Import all models to ensure they're registered with SQLAlchemy
from .user import User
from .guest import Guest
from .episode import Episode
from .appearance import Appearance

__all__ = ['User', 'Guest', 'Episode', 'Appearance']