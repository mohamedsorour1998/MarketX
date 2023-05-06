export interface User {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  password?: string;
  phone: string;
  address: string;
  city: string;
  state: string;
  zip_code: string;
  country: string;
  date_joined: Date;
  last_login: Date;
  is_staff: boolean;
}
