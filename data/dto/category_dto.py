from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from datetime import datetime

@dataclass
class CategoryDTO:
    """Data Transfer Object para Category"""
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convierte DTO a diccionario"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CategoryDTO':
        """Crea DTO desde diccionario"""
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            description=data.get('description'),
            created_at=data.get('created_at'),
            updated_at=data.get('updated_at')
        )
    
    @classmethod
    def from_entity(cls, category: 'Category') -> 'CategoryDTO':
        """Crea DTO desde entidad Category"""
        return cls(
            id=category.id,
            name=category.name,
            description=category.description,
            created_at=category.created_at.isoformat() if category.created_at else None,
            updated_at=category.updated_at.isoformat() if category.updated_at else None
        )
    
    def to_entity(self) -> 'Category':
        """Convierte DTO a entidad Category"""
        from models.category_model import Category
        return Category(
            id=self.id,
            name=self.name,
            description=self.description,
            created_at=datetime.fromisoformat(self.created_at) if self.created_at else None,
            updated_at=datetime.fromisoformat(self.updated_at) if self.updated_at else None
        )
