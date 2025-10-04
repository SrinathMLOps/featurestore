"""
Complete demo of feature engineering and feature store operations.

This script demonstrates an end-to-end workflow for:
1. Feature engineering from raw user activity data
2. Feature store initialization and configuration
3. Batch feature retrieval for model training
4. Online feature retrieval for model serving
"""

import sys
import os
import pandas as pd
from datetime import datetime, timedelta

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.feature_engineering import engineer_user_activity_features
from src.feature_store_ops import (
    initialize_feature_store,
    define_feature_view,
    simulate_historical_features,
    simulate_online_features
)


def main():
    """Run the complete feature store demo workflow."""
    
    print("=" * 80)
    print("Feature Store Demo: User Activity Features")
    print("=" * 80)
    print()
    
    # Step 1: Define sample raw user activity data
    print("Step 1: Defining raw user activity data...")
    raw_data = {
        'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5],
        'activity_type': ['view', 'view', 'purchase', 'view', 'view', 
                         'view', 'click', 'view', 'purchase', 'view', 'purchase', 'click'],
        'timestamp': [
            1704067200, 1704070800, 1704074400,  # User 1
            1704078000, 1704081600,              # User 2
            1704085200, 1704088800, 1704092400, 1704096000,  # User 3
            1704099600, 1704103200,              # User 4
            1704106800                           # User 5
        ],
        'product_id': ['A', 'B', 'A', 'C', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H']
    }
    print(f"  - Total records: {len(raw_data['user_id'])}")
    print(f"  - Unique users: {len(set(raw_data['user_id']))}")
    print()
    
    # Step 2: Engineer features from raw data
    print("Step 2: Engineering features from raw data...")
    features_df = engineer_user_activity_features(raw_data)
    print("  Engineered Features:")
    print(features_df.to_string(index=False))
    print()
    
    # Step 3: Initialize feature store
    print("Step 3: Initializing feature store...")
    feature_store = initialize_feature_store()
    print(f"  - Feature store initialized: {feature_store['initialized']}")
    print(f"  - Repository path: {feature_store['repo_path']}")
    print()
    
    # Step 4: Define and register feature view
    print("Step 4: Defining feature view...")
    feature_view = define_feature_view()
    print(f"  - Feature view name: {feature_view['name']}")
    print(f"  - Entity: {feature_view['entities']}")
    print(f"  - Features: {[f['name'] for f in feature_view['features']]}")
    print(f"  - TTL: {feature_view['ttl']}")
    print()
    
    # Step 5: Demonstrate historical feature retrieval (for training)
    print("Step 5: Demonstrating historical feature retrieval (Training Use Case)...")
    print("  This simulates fetching features for model training with point-in-time correctness.")
    
    # Create entity DataFrame with timestamps (typical training scenario)
    entity_df = pd.DataFrame({
        'user_id': [1, 2, 3, 4, 5],
        'event_timestamp': pd.to_datetime([
            datetime.now() - timedelta(days=i) for i in range(5)
        ])
    })
    
    historical_features = simulate_historical_features(
        entity_df,
        features=['total_activities', 'unique_products_viewed', 'purchase_count']
    )
    print("  Historical Features (for training):")
    print(historical_features.to_string(index=False))
    print()
    
    # Step 6: Demonstrate online feature retrieval (for serving)
    print("Step 6: Demonstrating online feature retrieval (Serving Use Case)...")
    print("  This simulates real-time feature lookup during model inference.")
    
    # Create entity rows (typical serving scenario)
    entity_rows = [
        {'user_id': 1},
        {'user_id': 3},
        {'user_id': 5}
    ]
    
    online_features = simulate_online_features(
        entity_rows,
        features=['total_activities', 'unique_products_viewed', 'purchase_count']
    )
    print("  Online Features (for serving):")
    print(online_features.to_string(index=False))
    print()
    
    # Summary
    print("=" * 80)
    print("Demo Complete!")
    print("=" * 80)
    print()
    print("Key Takeaways:")
    print("  1. Feature engineering transforms raw data into ML-ready features")
    print("  2. Feature stores provide centralized feature management")
    print("  3. Historical retrieval ensures point-in-time correctness for training")
    print("  4. Online retrieval enables low-latency serving for real-time predictions")
    print()
    print("Next Steps:")
    print("  - Explore the source code in src/feature_engineering.py")
    print("  - Review feature store operations in src/feature_store_ops.py")
    print("  - Check out the documentation in docs/")
    print()


if __name__ == "__main__":
    main()
