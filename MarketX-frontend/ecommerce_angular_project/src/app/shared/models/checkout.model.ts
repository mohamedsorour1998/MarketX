export interface Checkout {
  id: number;
  address: string;
  city: string;
  state: string;
  zip_code: string;
  country: string;
  product: string;
  quantity: number;
  date_ordered: string;
  is_complete: boolean;
  payment_method: string;
  user: number;
  order: number;
}
