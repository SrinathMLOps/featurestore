"""Feature engineering module for user activity data."""

from typing import Dict, List
import pandas as pd


def calculate_total_activities(raw_data: Dict[str, List]) -> Dict[int, int]:
    """
    Calculate total activities per user.
    
    Args:
        raw_data: Dictionary containing user activity records with keys:
                  'user_id', 'activity_type', 'timestamp', 'product_id'
    
    Returns:
        Dictionary mapping user_id to total activity count
        
    Raises:
        ValueError: If raw_data is missing required keys or has inconsistent lengths
    """
    if not raw_data or 'user_id' not in raw_data:
        raise ValueError("raw_data must contain 'user_id' key")
    
    activity_counts = {}
    for user_id in raw_data['user_id']:
        activity_counts[user_id] = activity_counts.get(user_id, 0) + 1
    
    return activity_counts


def calculate_unique_products_viewed(raw_data: Dict[str, List]) -> Dict[int, int]:
    """
    Calculate unique products viewed per user.
    
    Args:
        raw_data: Dictionary containing user activity records with keys:
                  'user_id', 'activity_type', 'timestamp', 'product_id'
    
    Returns:
        Dictionary mapping user_id to count of unique products viewed
        
    Raises:
        ValueError: If raw_data is missing required keys or has inconsistent lengths
    """
    required_keys = ['user_id', 'activity_type', 'product_id']
    for key in required_keys:
        if key not in raw_data:
            raise ValueError(f"raw_data must contain '{key}' key")
    
    user_products = {}
    for user_id, activity_type, product_id in zip(
        raw_data['user_id'], 
        raw_data['activity_type'], 
        raw_data['product_id']
    ):
        if activity_type == 'view':
            if user_id not in user_products:
                user_products[user_id] = set()
            user_products[user_id].add(product_id)
    
    return {user_id: len(products) for user_id, products in user_products.items()}


def calculate_purchase_count(raw_data: Dict[str, List]) -> Dict[int, int]:
    """
    Calculate purchase count per user.
    
    Args:
        raw_data: Dictionary containing user activity records with keys:
                  'user_id', 'activity_type', 'timestamp', 'product_id'
    
    Returns:
        Dictionary mapping user_id to purchase count
        
    Raises:
        ValueError: If raw_data is missing required keys or has inconsistent lengths
    """
    required_keys = ['user_id', 'activity_type']
    for key in required_keys:
        if key not in raw_data:
            raise ValueError(f"raw_data must contain '{key}' key")
    
    purchase_counts = {}
    for user_id, activity_type in zip(raw_data['user_id'], raw_data['activity_type']):
        if activity_type == 'purchase':
            purchase_counts[user_id] = purchase_counts.get(user_id, 0) + 1
    
    return purchase_counts


def engineer_user_activity_features(raw_data: Dict[str, List]) -> pd.DataFrame:
    """
    Engineer features from raw user activity data.
    
    This function takes raw user activity data and computes aggregated features
    including total activities, unique products viewed, and purchase counts per user.
    
    Args:
        raw_data: Dictionary containing user activity records with keys:
                  - 'user_id': List of user identifiers
                  - 'activity_type': List of activity types ('view', 'click', 'purchase')
                  - 'timestamp': List of Unix timestamps
                  - 'product_id': List of product identifiers
    
    Returns:
        pandas DataFrame with columns:
        - user_id: User identifier
        - total_activities: Total number of activities per user
        - unique_products_viewed: Count of unique products viewed per user
        - purchase_count: Number of purchases per user
        
    Raises:
        ValueError: If raw_data is missing required keys or has inconsistent array lengths
        
    Example:
        >>> raw_data = {
        ...     'user_id': [1, 1, 2, 2, 3],
        ...     'activity_type': ['view', 'purchase', 'view', 'view', 'click'],
        ...     'timestamp': [1609459200, 1609545600, 1609632000, 1609718400, 1609804800],
        ...     'product_id': ['A', 'A', 'B', 'C', 'D']
        ... }
        >>> features_df = engineer_user_activity_features(raw_data)
        >>> print(features_df)
    """
    # Validate input structure
    required_keys = ['user_id', 'activity_type', 'timestamp', 'product_id']
    for key in required_keys:
        if key not in raw_data:
            raise ValueError(f"Missing required key: {key}")
    
    # Validate data consistency
    lengths = [len(raw_data[key]) for key in required_keys]
    if len(set(lengths)) > 1:
        raise ValueError("All data arrays must have the same length")
    
    # Calculate features
    total_activities = calculate_total_activities(raw_data)
    unique_products = calculate_unique_products_viewed(raw_data)
    purchase_counts = calculate_purchase_count(raw_data)
    
    # Get all unique user IDs
    unique_users = sorted(set(raw_data['user_id']))
    
    # Build feature DataFrame
    features = {
        'user_id': unique_users,
        'total_activities': [total_activities.get(uid, 0) for uid in unique_users],
        'unique_products_viewed': [unique_products.get(uid, 0) for uid in unique_users],
        'purchase_count': [purchase_counts.get(uid, 0) for uid in unique_users]
    }
    
    return pd.DataFrame(features)
