select
    product_id,
    product_name,
    vendor,
    product_type,
    status,
    created_at,
    updated_at
from {{ ref('stg_products') }}