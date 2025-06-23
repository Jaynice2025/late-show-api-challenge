from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.appearance import Appearance
from models.guest import Guest
from models.episode import Episode
from app import db

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'JSON data is required'}), 400
        
        # Validate required fields
        required_fields = ['rating', 'guest_id', 'episode_id']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'{field} is required'}), 400
        
        # Validate rating range
        if not (1 <= data['rating'] <= 5):
            return jsonify({'error': 'Rating must be between 1 and 5'}), 400
        
        # Check if guest exists
        guest = Guest.query.get(data['guest_id'])
        if not guest:
            return jsonify({'error': 'Guest not found'}), 404
        
        # Check if episode exists
        episode = Episode.query.get(data['episode_id'])
        if not episode:
            return jsonify({'error': 'Episode not found'}), 404
        
        # Create appearance
        appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        
        db.session.add(appearance)
        db.session.commit()
        
        return jsonify(appearance.to_dict()), 201
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500