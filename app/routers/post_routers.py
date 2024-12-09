from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.post_shcmas import PostCreate, Post
from app.controllers.post import (
    create_post,
    get_post,
    get_posts,
    delete_post,
    update_post,
)
from app.database.database import get_db

router = APIRouter()

# Crear un post
@router.post("/", response_model=Post)
def create_post_endpoint(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db, post)

# Obtener un post por ID
@router.get("/{post_id}", response_model=Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = get_post(db, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return post

# Obtener todos los posts
@router.get("/", response_model=list[Post])
def read_posts(db: Session = Depends(get_db)):
    return get_posts(db)

# Actualizar un post
@router.put("/{post_id}", response_model=Post)
def update_post_endpoint(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    updated_post = update_post(db, post_id, post.dict())
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return updated_post

# Eliminar un post
@router.delete("/{post_id}")
def delete_post_endpoint(post_id: int, db: Session = Depends(get_db)):
    return delete_post(db, post_id)
