from sqlalchemy.orm import Session
from app.models.post_models import Post
from app.schemas.post_shcmas import PostCreate

def create_post(db: Session, post_data: PostCreate):
    db_post = Post(**post_data.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.post_id == post_id).first()

def get_posts(db: Session):
    return db.query(Post).all()

def delete_post(db: Session, post_id: int):
    post = get_post(db, post_id)
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}

def update_post(db: Session, post_id: int, post_data: dict):
    post = get_post(db, post_id)
    if not post:
        return None
    for key, value in post_data.items():
        setattr(post, key, value)
    db.commit()
    db.refresh(post)
    return post
