from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def example_data():
    """Create example data for the test database."""
    #FIXME: write a function that creates a game and adds it to the database.
    
    board_game = Game(game_id=1, name="scrabble", description="spelling game")
    puzzle_game = Game(game_id=2, name="jigsaw", description="put pieces together")
    maze_game = Game(game_id=3, name="treasure hunt", description="find path to treasure")

    db.session.add_all([board_game, puzzle_game, maze_game])
    db.session.commit()

def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print "Connected to DB."
 