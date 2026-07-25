select
    id as customer_id,
    state,
    orders_count,
    cast(total_spent as decimal(10,2)) as total_spent,
    verified_email,
    currency,
    tags,
    created_at,
    updated_at
from raw_customers