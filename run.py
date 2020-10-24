from lolgoal import app

from lolgoal import create_db_engine
from lolgoal.config import DbEngine_config

engine = create_db_engine(DbEngine_config)


app.config.from_object(DbEngine_config)

if __name__ == '__main__':
    app.run(debug=True)

