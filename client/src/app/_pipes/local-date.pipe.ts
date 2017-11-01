import { Pipe, PipeTransform, Injector, LOCALE_ID } from '@angular/core';
import { DatePipe } from '@angular/common';

@Pipe({
  name: 'localDate'
})
export class LocalDatePipe implements PipeTransform {
  constructor(private injector: Injector) {}
  transform(value: any, pattern?: string): any {
    const diff = new Date().getTimezoneOffset() * 60 * 1000;
    if (typeof value === 'number') {
      value -= diff;
    } else if (value instanceof Date) {
      value = new Date(value.getTime() - diff);
    }
    return new DatePipe(this.injector.get(LOCALE_ID)).transform(value, pattern);
  }
}
