from app import app
import views
import seed

if __name__ == '__main__':
    seed.seed()
    app.run()
