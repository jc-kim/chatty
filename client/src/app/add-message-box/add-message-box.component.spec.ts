import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddMessageBoxComponent } from './add-message-box.component';

describe('AddMessageBoxComponent', () => {
  let component: AddMessageBoxComponent;
  let fixture: ComponentFixture<AddMessageBoxComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddMessageBoxComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddMessageBoxComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
