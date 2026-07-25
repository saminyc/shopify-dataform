select
    customer_id,
    state,
    orders_count,
    total_spent,
    verified_email,
    currency,
    tags,
    created_at,
    updated_at
from {{ ref('stg_customers') }}