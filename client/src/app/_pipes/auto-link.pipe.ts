import { Pipe, PipeTransform } from '@angular/core';
import anchorme from 'anchorme';
import * as autolink from 'autolinker';

@Pipe({
  name: 'autoLink'
})
export class AutoLinkPipe implements PipeTransform {

  transform(value: any, options?: any): any {
    return autolink.link(value, options);
  }

}
