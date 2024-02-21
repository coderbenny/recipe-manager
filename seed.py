from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Recipe, Category, Author

if __name__ == '__main__':
    engine = create_engine('sqlite:///recipes.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    
    author1 = Author(name="John James")
    author2 = Author(name="Joyce Meyer")
    
    category1 = Category(title="Soup")
    category2 = Category(title="Dessert")
    
    session.add_all([author1, author2, category1, category2])
    session.commit()
    
    bone_soup = Recipe(name="Bone Soup", ingredients="Bone, water, salt", instructions="Boil bone in water, add salt to taste", category_id=category1.id, author_id=author1.id)
    chocolate_cake = Recipe(name="Chocolate Cake", ingredients="Flour, sugar, cocoa powder, eggs, milk", instructions="Mix all ingredients, bake in oven", category_id=category2.id, author_id=author2.id)
    spaghetti = Recipe(name="Spaghetti", ingredients="Pasta, tomato sauce, ground beef, onion, garlic", instructions="Cook pasta, brown ground beef with onion and garlic, add tomato sauce, mix with pasta", category_id=category1.id, author_id=author1.id)
    
    session.add_all([bone_soup, chocolate_cake, spaghetti])
    session.commit()



