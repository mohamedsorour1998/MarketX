export interface Checkout {
  first_name: string;
  last_name: string;
  email: string;
  address: string;
  city: string;
  state: string;
  zip: string;
  products: { product: number; quantity: number }[];
}
