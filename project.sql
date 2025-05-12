-- Active: 1745938775538@@127.0.0.1@5432@projectbasda@public
CREATE TABLE "user" (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    hire_date DATE,
    status VARCHAR(20) CHECK (status IN ('active', 'inactive', 'suspended')) DEFAULT 'active',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE role (
    role_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE user_role (
    user_id INT NOT NULL,
    role_id INT NOT NULL,
    assigned_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES "user"(user_id),
    FOREIGN KEY (role_id) REFERENCES role(role_id)
);
CREATE TABLE permission (
    permission_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE user_permission (
    user_id INT NOT NULL,
    permission_id INT NOT NULL,
    assigned_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, permission_id),
    FOREIGN KEY (user_id) REFERENCES "user"(user_id),
    FOREIGN KEY (permission_id) REFERENCES permission(permission_id)
);
CREATE TABLE shift (
    shift_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    day_of_week VARCHAR(10) CHECK (day_of_week IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES "user"(user_id)
);
CREATE TABLE inventory (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    quantity NUMERIC(10,2) NOT NULL,
    unit VARCHAR(20) NOT NULL,
    min_threshold NUMERIC(10,2) NOT NULL,
    supplier_info TEXT,
    last_restocked DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE menu_item (
    menu_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price NUMERIC(10,2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    photo_url VARCHAR(255),
    preparation_time INT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE ingredient (
    ingredient_id SERIAL PRIMARY KEY,
    menu_id INT NOT NULL,
    inventory_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    quantity_used NUMERIC(10,2) NOT NULL,
    unit VARCHAR(20) NOT NULL,
    FOREIGN KEY (menu_id) REFERENCES menu_item(menu_id),
    FOREIGN KEY (inventory_id) REFERENCES inventory(item_id)
);
CREATE TABLE review (
    review_id SERIAL PRIMARY KEY,
    menu_id INT NOT NULL,
    rating SMALLINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) CHECK (status IN ('pending', 'approved', 'rejected')) DEFAULT 'pending',
    response TEXT,
    FOREIGN KEY (menu_id) REFERENCES menu_item(menu_id)
);
CREATE TABLE "table" (
    table_id SERIAL PRIMARY KEY,
    table_number VARCHAR(20) NOT NULL UNIQUE,
    capacity INT NOT NULL,
    status VARCHAR(20) CHECK (status IN ('available', 'occupied', 'reserved', 'maintenance')) DEFAULT 'available',
    location VARCHAR(100)
);
CREATE TABLE "order" (
    order_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    order_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) CHECK (status IN ('pending', 'processing', 'completed', 'cancelled')) DEFAULT 'pending',
    total_amount NUMERIC(12,2) NOT NULL,
    payment_method VARCHAR(20) CHECK (payment_method IN ('cash', 'qris', 'e-wallet', 'credit_card', 'debit_card')) NOT NULL,
    payment_status VARCHAR(20) CHECK (payment_status IN ('pending', 'paid', 'failed', 'refunded')) DEFAULT 'pending',
    customer_notes TEXT,
    table_id INT,
    FOREIGN KEY (user_id) REFERENCES "user"(user_id),
    FOREIGN KEY (table_id) REFERENCES "table"(table_id)
);
CREATE TABLE order_detail (
    order_id INT NOT NULL,
    menu_id INT NOT NULL,
    quantity INT NOT NULL,
    subtotal NUMERIC(10,2) NOT NULL,
    notes TEXT,
    PRIMARY KEY (order_id, menu_id),
    FOREIGN KEY (order_id) REFERENCES "order"(order_id),
    FOREIGN KEY (menu_id) REFERENCES menu_item(menu_id)
);
CREATE TABLE payment (
    payment_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    amount NUMERIC(12,2) NOT NULL,
    payment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    transaction_id VARCHAR(100),
    payment_details JSONB,
    FOREIGN KEY (order_id) REFERENCES "order"(order_id)
);
CREATE TABLE reservation (
    reservation_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    reservation_date TIMESTAMP WITH TIME ZONE NOT NULL,
    party_size INT NOT NULL,
    status VARCHAR(20) CHECK (status IN ('confirmed', 'cancelled', 'completed', 'no-show')) DEFAULT 'confirmed',
    special_request TEXT,
    table_id INT,
    user_id INT,
    FOREIGN KEY (table_id) REFERENCES "table"(table_id),
    FOREIGN KEY (user_id) REFERENCES "user"(user_id)
);
CREATE TABLE promotion (
    promo_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    discount_type VARCHAR(20) CHECK (discount_type IN ('percentage', 'fixed_amount')) NOT NULL,
    discount_value NUMERIC(10,2) NOT NULL,
    start_date TIMESTAMP WITH TIME ZONE NOT NULL,
    end_date TIMESTAMP WITH TIME ZONE NOT NULL,
    status VARCHAR(20) CHECK (status IN ('active', 'inactive', 'expired')) DEFAULT 'active',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE menu_promotion (
    menu_id INT NOT NULL,
    promo_id INT NOT NULL,
    PRIMARY KEY (menu_id, promo_id),
    FOREIGN KEY (menu_id) REFERENCES menu_item(menu_id),
    FOREIGN KEY (promo_id) REFERENCES promotion(promo_id)
);
