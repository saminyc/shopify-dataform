select
    order_id,
    customer_id,
    order_name,
    order_number,

    cast(total_price as decimal(10,2)) as total_price,
    cast(subtotal_price as decimal(10,2)) as subtotal_price,
    cast(total_tax as decimal(10,2)) as total_tax,

    cast(created_at as timestamp) as created_at,
    cast(processed_at as timestamp) as processed_at,

    financial_status,
    currency

from {{ ref('stg_orders') }}