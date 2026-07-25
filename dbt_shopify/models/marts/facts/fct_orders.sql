select
    order_id,
    customer_id,
    order_name,
    order_number,
    financial_status,
    currency,
    total_price,
    subtotal_price,
    total_tax,
    created_at,
    processed_at
from {{ ref('stg_orders') }}