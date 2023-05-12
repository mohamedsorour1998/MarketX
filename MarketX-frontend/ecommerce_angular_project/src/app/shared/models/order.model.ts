import { Product } from './product.model';

export interface Order {
  id: number;
  quantity: number;
  is_complete: boolean;
  user: number;
  product: number;
}
