select
    id as order_id,
    "customer.id" as customer_id,
    name as order_name,
    order_number,
    financial_status,
    currency,
    cast(total_price as decimal(10,2)) as total_price,
    cast(subtotal_price as decimal(10,2)) as subtotal_price,
    cast(total_tax as decimal(10,2)) as total_tax,
    created_at,
    processed_at,
    updated_at
from raw_orders