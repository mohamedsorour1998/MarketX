import { AbstractControl, FormGroup, ValidatorFn } from '@angular/forms';

export function MustMatch(passwordControl: AbstractControl): ValidatorFn {
  return (
    confirmPasswordControl: AbstractControl
  ): { [key: string]: boolean } | null => {
    if (
      !passwordControl ||
      !confirmPasswordControl ||
      passwordControl.value === confirmPasswordControl.value
    ) {
      return null;
    } else {
      return { mismatch: true };
    }
  };
}
