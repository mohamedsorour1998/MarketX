import { Product } from './product.model';

export interface Order {
  id: number;
  user: number;
  products: Product[];
  total: number;
  created_at: Date;
  updated_at: Date;
}
